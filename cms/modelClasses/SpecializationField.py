from django.db import models

class SpecializationField(models.Model):
	facultyId = models.CharField(max_length=100, blank=False, null=False)
	fieldName = models.CharField(max_length=200, blank=False, null=False)

	def __str__(self):
		return self.facultyId