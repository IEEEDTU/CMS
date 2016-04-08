from django.db import models

class WebLink(models.Model):
	webLinkId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
	link = models.URLField(max_length=200, null=False, blank=False)