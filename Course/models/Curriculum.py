from django.db import models
from Profiler.models import Student
from Course.models import *

class CurriculumManager(models.Manager):
    def retrieveCurriculum(self, request):
        C = Course.objects.get(courseId = request['courseId'])
        objlist  = Curriculum.objects.filter(course = C)
        return objlist 

class Curriculum(models.Model):
    #Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = False)
    #Unit
    unit = models.PositiveIntegerField()
    #description
    description = models.TextField()
    
    objects = CurriculumManager()
    
    def __str__(self):
        return str(self.course)
    