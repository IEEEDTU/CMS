from django.db import models

class Address(models.Model):
	locality = models.CharField(max_length=100, blank=False, null=False)
	city = models.CharField(max_length=50, blank=False, null=False)
	state = models.CharField(max_length=50, blank=False, null=False)
	country = models.CharField(max_length=50, blank=False, null=False)
	pincode = models.IntegerField()

	def __str__(self):
		return self.state