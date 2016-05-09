from django.db import models
from .Student import *
from .InterestField import *


class StudentFieldManager(models.Manager):
    def addStudentField(self, request):
        """ adds new student interest field """
        SF = StudentField(
            student=Student.objects.getStudentByRegIdOrRollNo(request),
            field=Field.objects.get(fieldName=request['fieldName'])
        )
        SF.save()
        return SF

    def deleteStudentField(self, request):
        """ deletes student interest field """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        F = Field.objects.get(fieldName=request['fieldName'])
        SF = StudentField.objects.get(student=S, field=F)
        SF.delete()
        return SF

    def retrieveStudentField(self, request):
        """ retrieve interest fields of a student """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        SF = StudentField.objects.filter(student=S)
        return SF


class StudentField(models.Model):
    # student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # field
    field = models.ForeignKey(Field, on_delete=models.CASCADE, default=False)

    objects = StudentFieldManager()

    def __str__(self):
        return str(self.student) + " - " + self.field
