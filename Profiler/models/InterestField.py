from django.db import models

class FieldManager(models.Manager):
	def addField(self, request):
		F = Field(fieldName = request['fieldName'])
		F.save()
		return F
	
	def deleteField(self, request):
		F = Field.objects.get(fieldName = request['fieldName'])
		F = F.delete()
		return F
	
	def retrieveFields():
		pass

class Field(models.Model):
	# Specialization Field
	fieldName = models.CharField(max_length=200, blank=False, null=False)

	objects = FieldManager()

	def __str__(self):
		return self.fieldName
