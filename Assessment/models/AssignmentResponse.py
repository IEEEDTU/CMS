from django.db import models
from Profiler.models import Student
from Course.models import *
from .Score import *

class AssignmentResponseManager(models.Model):
    def addAssignmentResponse(self, request):
        AR = AssignmentResponse(
            link = request['responseLink'],
            course = Course.objects.get(courseId = request['courseId']),
            student = Student.objects.get(rollNo = request['rollNo']),
            grade = request['grade'],
            submisionDate = request['submissionDate'],
            status = request['status']
        )
        AR.save()
        return AR
        
    def editAssignmentResponse(self, request):
        AR = AssignmentResponse.objects.get(responseLink = request)
        AR.responseLink = request['responseLink']
        AR.grade = request['grade']
        AR.submissionDate = request['submissionDate']
        AR.status = request['status']
        AR.save()
        return AR 
        
    def deleteAssignmentResponse(self, request):
        AR = AssignmentResponse.objects.get(responseLink = request['responseLink'])
        AR.delete()
        return AR
        
    def retrieveAssignments(self, request):
        C = Course.objects.get(courseId = request['courseId'])
        S = Student.objects.get(rollNo = request['rollNo'])
        objList = AssignmentResponse.objects.filter(course = C).filter(student = S)
        return objList
            
class AssignmentResponse(models.Model):
    #response link
    responseLink = models.URLField(max_length=200)
    #Course
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default = False)
    #Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default = False)
    #grade
    grade = models.CharField(max_length=1)
    #submission date
    submissionDate = models.DateField(auto_now=False,auto_now_add=True)
    #status
    status = models.CharField(max_length = 50)
    
    def __str__(self):
        return str(self.responseLink)