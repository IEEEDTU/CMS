from django.db import models
#from Profiler.models import Faculty


class DepartmentManager(models.Manager):
    def addDepartment(self, request):
        """ adds new department """
        D = Department(
            deptId=request['deptId'],
            deptName=request['deptName'],
            hod=request['hod'],
            email=request['email'],
            location=request['location'],
            branchCount=request['branchCount'],
            studentStrength=request['studentStrength'],
            facultyStrength=request['facultyStrength'])
        D.save()
        return D

    def getDepartmentById(self, request):
        """ get the department details on the basis of deptId """
        D = Department.objects.get(deptId=request["deptId"])
        return D

    def deleteDepartment(self, request):
        """ get the department details on the basis of deptId """
        D = Department.objects.get(deptId=request["deptId"])
        D = D.delete()
        return D

class Department(models.Model):
    # Department ID
    deptId = models.CharField(max_length=5, primary_key=True, blank=False, null=False)
    # Department name
    deptName = models.CharField(max_length=50)
    # Head of the department
    #hod = models.CharField(max_length=50)
    hod = models.ForeignKey('Profiler.Faculty', related_name="head_of_dept", on_delete = models.CASCADE, default=False)
    # Email address
    email = models.EmailField()
    # Location
    location = models.CharField(max_length=100)
    # Branch count
    branchCount = models.PositiveIntegerField()
    # Student's strength
    studentStrength = models.PositiveIntegerField()
    # Faculty's strength
    facultyStrength = models.PositiveIntegerField()

    objects = DepartmentManager()

    def __str__(self):
        return self.deptId + " - " + self.deptName
