from django.db import models
from .Course import *
from .Group import *
#from Profiler.models import Faculty

class CourseGroupManager(models.Manager):
    def retrieveCourseGroups(self, request):
        C = Course.objects.getCourseById(request)
        G = Group.objects.getGroupById(request)
        objlist = CourseGroup.objects.filter(course = C, group = G)
        return objlist
    
    def addCourseGroup(self, request):
        C = Course.objects.getCourseById(request)
        G = Group.objects.getGroupById(request)
        F = Faculty.objects.get(facultyId = request["facultyId"])
        CG = CourseGroup(
                course = C,
                group = G,
                instructor = F
            )
        CG.save()
        return CG
    
    def deleteCourseGroup(self, request):
        CG = CourseGroup.objects.get(id = request['id'])
        CG = CG.delete()
        return CG
    
    def editCourseGroup(self, request):
        F = Faculty.objects.get(facultyId = request["facultyId"])
        CG = CourseGroup.objects.get(id = request['id'])
        CG.instructor = F
        CG.save()
        return CG
    
    def getCourseGroupById(self, request):
        CG = CourseGroup.objects.get(id = request['id'])
        return CG

class CourseGroup(models.Model):
    # Course
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default=False)
    # Group
    group = models.ForeignKey(Group, on_delete = models.CASCADE, default=False)
    # Instructor
    instructor = models.ForeignKey('Profiler.Faculty',  on_delete = models.CASCADE)
    
    objects = CourseGroupManager()
    
    def __str__(self):
        return self.course + " - " + self.group
