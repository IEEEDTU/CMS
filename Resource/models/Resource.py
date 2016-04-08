from django.db import models
from Course.models import Course
from Profiler.models import Faculty

class Resource(models.Model):
	BOOK = 0
	PUBLICATION = 1
	DOCUMENT = 2
	WEBLINK = 3
	RESOURCE_TYPE_CHOICES = ( (BOOK, 'Book'), (PUBLICATION, 'Publication'), (DOCUMENT, 'Document'), (WEBLINK, 'Web Links') )
	
	resourceId = models.AutoField(primary_key=True, blank=False, null=False)
	type = models.PositiveIntegerField(choices = RESOURCE_TYPE_CHOICES, blank=False, null=False)
	course = models.ForeignKey(Course, on_delete = models.CASCADE, default=False)
	updatedOn = models.DateTimeField(auto_now=True)
	updatedBy = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=False)
	