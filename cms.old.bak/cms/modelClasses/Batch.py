from django.db import models
from django.core import serializers

class BatchManager(models.Manager):
	def addBatch(self, req):
		self.batchType = req['batchType']
		# self.degree = req['degree']
		# self.dept = req['dept']
		self.strength = req['strength']
		
		batch = Batch(self.batchType,
						# self.degree,
						# self.dept,
						self.strength)
		batch.save()
		return Course.objects.latest(batchId)
		
	def deleteBatch(self, batchId):
		batch = Batch.objects.filter(batchId = batchId)
		if batch.delete():
			return True
		else:
			return False
			
	def getBatch(self, req):
		if 'batchId' in req:
			batch = Batch.objects.get(batchId = req['batchId'])
		elif 'batchType' in req:
			batch = Batch.objects.filter(batchType = req['batchType'])
		else:
			batch = Batch.objects.all()
		s = serializers.serialize('json', batch)
		return s
	
	# def getBatchByDegree(self, degree):
	# 	batch = Batch.objects.filter(degree = degree)
	# 	s = serializers.serialize('json', batch)
	# 	return s
		
	# def getBatchByDept(self, dept):
	# 	batch = Batch.objects.filter(dept = dept)
	# 	s = serializers.serialize('json', batch)
	# 	return s
		
	
		
class Batch(models.Model):
	batchId = models.CharField(max_length=20, blank=False, null=False)
	batchType = models.CharField(max_length=5, blank=False, null=False)
	# degree = models.ForeignKey(
	# 	'Degree',
	# 	on_delete = models.CASCADE,
	# )
	# dept = models.ForeignKey(
	# 	'Department',
	# 	on_delete = models.CASCADE,
	# )
	strength = models.IntegerField()
	
	objects = BatchManager()

	def __str__(self):
		return self.batchId