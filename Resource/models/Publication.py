from django.db import models

class Publication(models.Model):
	publicationId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
	title = models.CharField(max_length=50, blank=False, null=False)
	authors = models.CharField(max_length=50)
	publicationDate = models.DateField()
	organization = models.CharField(max_length=50)
	webLink = models.URLField(max_length=200)
	
	