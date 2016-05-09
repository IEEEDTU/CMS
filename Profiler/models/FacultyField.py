from django.db import models
from .Faculty import *
from .InterestField import *


class FacultyFieldManager(models.Manager):
    def addFacultyField(self, request):
        """ adds new faculty interest field """
        FF = FacultyField(
            faculty=Faculty.objects.getFacultyByRegIdOrFacultyId(request),
            field=Field.objects.get(fieldName=request['fieldName'])
        )
        FF.save()
        return FF

    def deleteFacultyField(self, request):
        """ deletes faculty interest field """
        F = Faculty.objects.getFacultyByRegIdOrFacultyId(request),
        IF = Field.objects.get(fieldName=request['fieldName'])
        FF = FacultyField.objects.get(faculty=F, field=IF)
        FF.delete()
        return FF

    def retrieveFacultyField(self, request):
        """ retrieve interest fields of a faculty """
        F = Faculty.objects.getFacultyByRegIdOrFacultyId(request),
        FF = FacultyField.objects.filter(faculty=F)
        return FF


class FacultyField(models.Model):
    # faculty
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=False)
    # field
    field = models.ForeignKey(Field, on_delete=models.CASCADE, default=False)

    objects = FacultyFieldManager()

    def __str__(self):
        return str(self.faculty) + " - " + self.field
