from django.db import models
from .Faculty import *

class Field(models.Model):
    # Faculty
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=False)
	# Specialization Field
    fieldName = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):  
        return self.fieldName