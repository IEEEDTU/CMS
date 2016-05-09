from django.db import models


class FieldManager(models.Manager):
    def addField(self, request):
        """ add new field """
        F = Field(fieldName=request['fieldName'])
        F.save()
        return F

    def deleteField(self, request):
        """ delete field """
        F = Field.objects.get(fieldName=request['fieldName'])
        F = F.delete()
        return F

    def retrieveFields(self, request):
        """ retrieve fields """
        F = Field.objects.all()
        return F


class Field(models.Model):
    # Specialization Field
    fieldName = models.SlugField(max_length=200, blank=False, null=False)

    objects = FieldManager()

    def __str__(self):
        return self.fieldName
