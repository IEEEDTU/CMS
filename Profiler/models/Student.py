from django.db import models
from .Person import *
from Course.models import Degree, Branch


class StudentManager(models.Manager):
    def addStudent(self, request):
        """inserts person details in the database"""
        nameObjs = Name.objects.addName(request)
        addressObjs = Address.objects.addAddress(request)
        contactObjs = Mobile.objects.addContacts(request)
        degreeObj = Degree.objects.get(degreeCode=request['degreeCode'])

        S = Student(
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
            rollNo=request['rollNo'],
            branch=Branch.objects.get(branchCode=request['branchCode']),
            degree=degreeObj,
            admissionYear=request['admissionYear'],
            graduationYear=request['admissionYear'] + degreeObj.duration,
            password=request['password'],
        )
        S.save()
        return S

    def getStudentByRegId(self, request):
        """ To get the object of student by its dtuRegId """
        S = Student.objects.get(dtuRegId=request["dtuRegId"])
        return S

    def getStudentByRollNo(self, request):
        """ To get the object of student by its rollNo """
        S = Student.objects.get(rollNo=request["rollNo"])
        return S

    def getStudentByRegIdOrRollNo(self, request):
        """ To get the object of student by its dtuRegId or roll no, whatever specified in request """
        if "dtuRegId" in request.keys():
            S = Student.objects.get(dtuRegId=request["dtuRegId"])
        else:
            S = Student.objects.get(rollNo=request["rollNo"])
        return S

    def getStudentByName(self, request):
        """ To get the objects of student by its name """
        N = Name.objects.get(preferredName=request['preferredName'])
        S = Student.objects.get(name=N)
        return S

    def retrieveStudents(self, request):
        """ retrieve students on the basis of degree, branch, admissionYear, graduationYear, category """
        S = Student.objects.all()
        if "degreeCode" in request.keys():
            D = Degree.objects.get(degreeCode=request["degreeCode"], degreeType=request["degreeType"])
            S = S.filter(degree=D)
        if "branchCode" in request.keys():
            B = Branch.objects.get(branchCode=request["branchCode"])
            S = S.filter(branch=B)
        if "admissionYear" in request.keys():
            S = S.filter(admissionYear=request["admissionYear"])
        if "graduationYear" in request.keys():
            S = S.filter(graduationYear=request["graduationYear"])
        if "category" in request.keys():
            S = S.filter(category=request["category"])

        return S

    def deleteStudent(self, request):
        """ deletes student on basis of dtuRegId or rollNo """
        if 'dtuRegId' in request.keys():
            S = Student.objects.get(dtuRegId=request['dtuRegId'])
            S = S.delete()
        if 'rollNo' in request.keys():
            S = Student.objects.get(dtuRegId=request['rollNo'])
            S = S.delete()
        return S


class Student(Person):
    # Roll number
    rollNo = models.CharField(max_length=30, primary_key=False, blank=False, null=False)
    # Branch of the student
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=False)
    # Degree programme of the student
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, default=False)
    # Year of admission
    admissionYear = models.PositiveIntegerField()
    # Year of graduation
    graduationYear = models.PositiveIntegerField()
    # Library ID
    libraryId = models.CharField(max_length=30, blank=True, null=True)
    # Login's password
    password = models.CharField(max_length=100, blank=False, null=False)

    objects = StudentManager()

    def __str__(self):
        return self.rollNo + " - " + str(self.name)
