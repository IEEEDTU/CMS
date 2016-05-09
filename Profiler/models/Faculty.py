from django.db import models
from .Person import *
from Course.models import Department


class FacultyManager(models.Manager):
    def addFaculty(self, request):
        """ adds new faculty member """
        nameObjs = Name.objects.addName(request)
        addressObjs = Address.objects.addAddress(request)
        contactObjs = Mobile.objects.addContacts(request)
        departmentObj = Department.objects.get(deptId=request['deptId'])

        F = Faculty(
            dtuRegId=request["dtuRegId"],
            name=nameObjs[0],
            permanentAdd=addressObjs[0],
            presentAdd=addressObjs[1],
            guardianAdd=addressObjs[2],
            personalMobile=contactObjs[0],
            alternativeMobile=contactObjs[1],
            personalEmail=request["personalEmail"],
            alternativeEmail=request["alternativeEmail"],
            dateOfBirth=request["dateOfBirth"],
            gender=request["gender"],
            category=request["category"],
            nationality=request["nationality"],
            religion=request["religion"],
            dormitory=request["dormitory"],
            fatherName=nameObjs[1],
            motherName=nameObjs[2],
            facultyId=request['facultyId'],
            designation=request['designation'],
            dateOfJoining=request['dateOfJoining'],
            jobType=request['jobType'],
            department=request['department'],
            libraryId=request['libraryId'],
            password=request['password'],
        )
        F.save()
        return F

    def getFacultyByRegId(self, request):
        """ To get the object of faculty by its dtuRegId """
        F = Faculty.objects.get(dtuRegId=request["dtuRegId"])
        return F

    def getFacultyByFacultyId(self, request):
        """ To get the object of faculty by its dtuRegId """
        F = Faculty.objects.get(facultyId=request["facultyId"])
        return F

    def getFacultyByRegIdOrFacultyId(self, request):
        """ To get the object of faculty by its dtuRegId or facultyId, whatever specified in request """
        if "dtuRegId" in request.keys():
            F = Faculty.objects.get(dtuRegId=request["dtuRegId"])
        else:
            F = Faculty.objects.get(facultyId=request["facultyId"])
        return F

    def getFacultyByName(self, request):
        """ To get the objects of student by its name """
        N = Name.objects.get(preferredName=request['preferredName'])
        F = Faculty.objects.get(name=N)
        # rollNoList = []
        # for n in N:
        #   S = Student.objects.filter(name = n)
        #   for s in S:
        #       rollNoList.append(s.rollNo)
        return F

    def deleteFaculty(self, request):
        if "dtuRegId" in request.keys():
            F = Faculty.objects.get(dtuRegId=request['dtuRegId'])
        elif "facultyId" in request.keys():
            F = Faculty.objects.get(facultyId=request['facultyId'])
        F = F.delete()
        return F

    def retrieveFaculty(self, request):
        """ retrieve IDs of all the courses depending on the request """
        """ note: department is must """
        """ other optional attributes: dateOfJoining, jobType """
        D = Department.objects.get(deptId=request['deptId'])
        objList = Faculty.objects.filter(department=D)

        if "dateOfJoining" in request.keys():
            objList = objList.objects.filter(dateOfJoining=request['dateOfJoining'])
        if "jobType" in request.keys():
            objList = objList.objects.filter(jobType=request['jobType'])

        idList = []

        for obj in objList:
            idList.append(obj.facultyId)

        return idList


class Faculty(Person):
    # Faculty's Identity
    facultyId = models.CharField(max_length=50, primary_key=False, blank=False, null=False)
    # Designation
    designation = models.CharField(max_length=50, blank=False, null=False)
    # Date of joining
    dateOfJoining = models.DateField()
    # Job Type (E.g.: Permanent, Guest)
    jobType = models.CharField(max_length=50, blank=False, null=False)
    # Department
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    # Salary
    # salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    # Library ID
    libraryId = models.CharField(max_length=30, blank=False, null=False)
    # Login's password
    password = models.CharField(max_length=100, blank=False, null=False)

    objects = FacultyManager()

    def __str__(self):
        return self.facultyId + " - " + str(self.name)
