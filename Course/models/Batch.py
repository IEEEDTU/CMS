from django.db import models
from .Department import *
from .AcademicDegree import *

class BatchManager(models.Manager):
	def addBatch(self, request):
		B = Batch(
			batchType = request['batchType'],
			degree = request['degree'],
			dept = request['dept'],
			strength = request['strength']
			)
		B.save()
		return True
		
	def deleteBatch(self, request):
		B = Batch.objects.filter(batchId = request['batchId'])
		B = B.get(batchType = request['batchType'])
		B = B.delete():
		return B
	
	def getBatchById(self, request):
		""" get the batch object using the batchId """
		B = Batch.objects.filter(batchId = request['batchId'])
		B = B.get(batchType = request['batchType'])
		return B
	
	def getBatchByDegree(self, degree):
		B = Batch.objects.filter(degree = degree)
		nameList = []
		for b in B
			nameList.append(b.batchId + "-" + b.batchType)
		return nameList
		
	def getBatchByDept(self, dept):
		B = Batch.objects.filter(dept = dept)
		nameList = []
		for b in B
			nameList.append(b.batchId + "-" + b.batchType)
		return nameList
	
class Batch(models.Model):
    # Batch ID
    batchId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
	# Batch Type A or B
    batchType = models.CharField(max_length=5, blank=False, null=False)
    # Degree
    degree = models.ForeignKey(Degree, on_delete = models.CASCADE, default=False)
	# Department
    department = models.ForeignKey(Department, on_delete = models.CASCADE, default=False)
    # Batch strength
    strength = models.PositiveIntegerField()

	objects = BatchManager()
    
    def __str__(self):
        return self.batchId
