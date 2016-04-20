from django.db import models
from Profiler.models import Student
from Course.models import *

class AssignmentManager(models.Manager):
    def addAssignment(self, request):
        A = Assignment(
            link = request['link'],
            course = Course.objects.get(courseId = request['courseId']),
            deadline = request['deadline'],
            comments = request['comments'],
            publishedDate = request['publishedDate']
        )
        
        A.save()
        return A
        
    def editAssignment(self, request):
        A = Assignment.objects.get(link = request['link'])
        A.link = request['link']
        A.deadline = request['deadline']
        A.comments = request['comments']
        A.publishedDate = request['publishedDate']
        A.save()
        return A
        
    def deleteAssignment(self, request):
        A = Assignment.objects.get(link = request['link'])
        A.delete()
        return A
        
    def retrieveAssignments(self, request):
        C = Course.objects.get(courseId = request['courseId'])
        objlist = Assignment.objects.filter(course = C)
        return objlist

class Assignment(models.Model):
    #Link
    link = models.URLField(max_length=200)
    #course
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default = False)
    #deadline
    deadline = models.DateField(auto_now=False, auto_now_add=True)
    #comments
    comments = models.TextField()
    #published_date
    publishedDate = models.DateField(auto_now=False, auto_now_add=True)
    
    objects = AssignmentManager()
    
    def __str__(self):
        return str(self.link)
    
    