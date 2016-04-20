from django.db import models
from .Department import *
from .AcademicDegree import *

class BranchManager(models.Manager):
    def addBranch(self, request):
        """ add new branch """
        B = Branch(
            branchCode=request['branchCode'],
            branchName=request['branchName'],
            seatsAvailable=request['seatsAvailable'],
            degree=Degree.objects.get(degreeCode=request['degreeCode']),
            department=Department.objects.get(deptId=request['deptId'])
        )
        B.save()
        return B

    def editBranch(self, request):
        """ edit existing branch on the basis of branch code """
        """ note: degree is not an editable """
        B = Branch.objects.get(branch=request["branchCode"])
        B.branchName = request["branchName"]
        B.seatsAvailable = request["seatsAvailable"]
        D = Department.get(deptId=request["deptId"])
        B.department = D
        B.save()
        return B

    def deleteBranch(self, request):
        """ deletes any existing branch on the basis of branch code """
        B = Branch.objects.get(branchCode=request["branchCode"])
        B = B.delete()
        return B

    def getBranchByCode(self, request):
        """ get the branch details on the basis of branch code """
        B = Branch.objects.get(branchCode=request['branchCode'])
        return B

    def retrieveBranches(self, request):
        """ retrieve IDs of all the courses depending on the request """
        """ note: degree is must """
        """ other optional attributes: department """
        D = Degree.objects.get(degreeCode=request["degreeCode"], degreeType=request["degreeType"])
        B = Branch.objects.filter(degree=D)
        if "deptId" in request.keys():
            D = Department.objects.get(deptId=request["deptId"])
            B = B.filter(department=D)

        # idList = []
        # for obj in B:
        #    idList.append(obj.courseId)
        return B


class Branch(models.Model):
    # Branch code
    branchCode = models.CharField(max_length=10, primary_key=True, blank=False, null=False)
    # Branch name
    branchName = models.CharField(max_length=100)
    # Seats available
    seatsAvailable = models.PositiveIntegerField()
    # Degree
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, default=False)
    # Department
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)

    objects = BranchManager()

    def __str__(self):
        return self.branchCode + " - " + self.branchName
