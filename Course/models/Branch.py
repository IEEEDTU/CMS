from django.db import models
from .Department import *
from .AcademicDegree import *

class BranchManager(models.Manager):
	def addBranch(self, request):
		B = Branch(
			branchCode = request['branchCode'],
			branchName = request['branchName'],
			seatsAvailable = request['seatsAvailable'],
			degree = Degree.objects.get(degreeCode = request['degreeCode']),
			department = Department.objects.get(deptId = request['deptId'])
			)
		B.save()
		return B
		
	def getBranch(self, request):
		""" get the branch details using branchCode"""
		B = Branch.objects.get(branchCode = request['branchCode'])
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

b0 = {
	'branchCode': 'SE',
	'branchName': 'Software Engineering',
	'seatsAvailable': '100',
	'degreeCode': 'BTECH',
	'deptId': 'CSEX'
	}