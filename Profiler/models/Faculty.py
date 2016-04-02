from django.db import models
from .Person import *
from Course.models import Department

class Faculty(Person):
    # Faculty's Identity
    facultyId = models.CharField(max_length=50, primary_key=False, blank=False, null=False)
    # Designation
    designation = models.CharField(max_length=50, blank=False, null=False)
    # Date of joining
    dateOfJoining = models.DateField()
    # Job Type (E.g.: Permanent, Guest)
    jobType = models.CharField(max_length=50, blank=False, null=False)
    # Department
    department = models.ForeignKey(Department, on_delete = models.CASCADE, default=False)
	# Salary
    # salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    # Library ID
    libraryId = models.CharField(max_length=30, blank=False, null=False)
    # Login's password
    password = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.facultyId + " - " + self.name