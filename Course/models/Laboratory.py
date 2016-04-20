from django.db import models
from .Department import *

class Laboratory(models.Model):
    # Laboratory code
    labCode = models.CharField(max_length=10, primary_key=True, blank=False, null=False)
    # Laboratory name
    labName = models.CharField(max_length=100)
    # Lab incharge
    incharge = models.CharField(max_length=50)
    # Department
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    # Location
    location = models.CharField(max_length=100)
    # Capacity
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.labCode + " - " + self.labName
