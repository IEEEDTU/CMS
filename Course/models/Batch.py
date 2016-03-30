from django.db import models
from .Department import *
from .AcademicDegree import *

class BatchManager(models.Manager):
	def addBatch(self, request):
		batch = Batch(
			batchType = request['batchType'],
			degree = request['degree'],
			dept = request['dept'],
			strength = request['strength']
			)
		batch.save()
		return True
		
	def deleteBatch(self, batchId):
		batch = Batch.objects.filter(batchId = batchId)
		if batch.delete():
			return True
		else:
			return False
			
	def getBatch(self, request):
		""" get the batch object using the batchId """
		B = Batch.objects.get(batchId = request['batchId'])
		return B
	
	def getBatchByDegree(self, degree):
		batch = Batch.objects.filter(degree = degree)
		#s = serializers.serialize('json', batch)
		return batch
		
	def getBatchByDept(self, dept):
		batch = Batch.objects.filter(dept = dept)
		#s = serializers.serialize('json', batch)
		return batch


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

	#objects = BatchManager()
    
    def __str__(self):
        return self.batchId

#class BatchManager(models.Manager):
#	def addBatch(self, request):
#		self.batchType = request['batchType']
#		# self.degree = request['degree']
#		# self.dept = request['dept']
#		self.strength = request['strength']
#
#		batch = Batch(self.batchType,
#						# self.degree,
#						# self.dept,
#						self.strength)
#		batch.save()
#		return Course.objects.latest(batchId)
#		
#	def deleteBatch(self, batchId):
#		batch = Batch.objects.filter(batchId = batchId)
#		if batch.delete():
#			return True
#		else:
#			return False
#			
#	def getBatch(self, request):
#		if 'batchId' in request:
#			batch = Batch.objects.get(batchId = request['batchId'])
#		elif 'batchType' in request:
#			batch = Batch.objects.filter(batchType = request['batchType'])
#		else:
#			batch = Batch.objects.all()
#		s = serializers.serialize('json', batch)
#		return s
#	
#	# def getBatchByDegree(self, degree):
#	# 	batch = Batch.objects.filter(degree = degree)
#	# 	s = serializers.serialize('json', batch)
#	# 	return s
#		
#	# def getBatchByDept(self, dept):
#	# 	batch = Batch.objects.filter(dept = dept)
#	# 	s = serializers.serialize('json', batch)
#	# 	return s
