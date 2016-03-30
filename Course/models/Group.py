from django.db import models
from .Branch import *

class Group(models.Model):
    # Group ID
    groupId = models.CharField(max_length=20, blank=False, null=False)
	# Semester
    semester = models.IntegerField()
	# Starting roll number
    startRollNo = models.CharField(max_length=20, blank=False, null=False)
	# Ending roll number
    endRollNo = models.CharField(max_length=20, blank=False, null=False)
	# Branch
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE, default=False)
	# Strength of the group
    strength = models.PositiveIntegerField()
    
    def __str__(self):
        return self.groupId