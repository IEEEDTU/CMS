from django.db import models
from .Department import *
from .AcademicDegree import *

class BatchManager(models.Manager):
    def addBatch(self, request):
        """ add new batch """
        B = Batch(
            batchType=request['batchType'],
            degree=request['degree'],
            dept=request['dept'],
            strength=request['strength'])
        B.save()
        return B

    def deleteBatch(self, request):
        """ deletes existing batch on the basis of batch ID """
        B = Batch.objects.get(batchId=request['batchId'])
        B = B.delete()
        return B

    def getBatchById(self, request):
        """ get the batch object using the batch ID """
        B = Batch.objects.get(batchId=request['batchId'])
        return B

    def retrieveBatches(self, request):
        """ get batches by type """
        """ note: type is optional field """
        B = Batch.objects.all()
        if 'batchType' in request.keys():
            B = Batch.objects.filter(batchType=request["batchType"])

        # idList = []
        # for b in B:
        #    idList.append(b.batchId + "-" + b.batchType)
        return B

class Batch(models.Model):
    # Batch ID
    batchId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
    # Batch Type A or B
    batchType = models.CharField(max_length=5, blank=False, null=False)
    # Degree
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, default=False)
    # Department
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    # Batch strength
    strength = models.PositiveIntegerField()

    objects = BatchManager()

    def __str__(self):
        return self.batchId
