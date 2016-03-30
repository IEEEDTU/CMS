from django.db import models

class Name(models.Model):
	fname = models.CharField(max_length=100, blank=False, null=False)
	mname = models.CharField(max_length=100, blank=False, null=False)
	lname = models.CharField(max_length=100, blank=False, null=False)
	preferredName = models.CharField(max_length=100, blank=False, null=False)

	def __str__(self):
		return self.preferredName