from django.db import models
from Profiler.models import Student
from Course.models import *


class AssignmentManager(models.Manager):
    def __getChar__(self, num):
        char = num
        return char

    def __generateAssignmentCode__(self, request):
        """ generates assignment ID on the basis of course """
        code = request['courseId']
        C = Course.objects.getCourseById(request)

        return code

    def addAssignment(self, request):
        """ add new assignment """
        C = Course.objects.get(courseId=request['courseId'])
        A = Assignment(
            link=request['link'],
            course=C,
            deadline=request['deadline'],
            comments=request['comments'],
            publishedDate=request['publishedDate']
        )

        A.save()
        return A

    def editAssignment(self, request):
        """ edit the assignment """
        A = Assignment.objects.get(link=request['link'])
        A.link = request['link']
        A.deadline = request['deadline']
        A.comments = request['comments']
        A.publishedDate = request['publishedDate']
        A.save()
        return A

    def deleteAssignment(self, request):
        A = Assignment.objects.get(link=request['link'])
        A.delete()
        return A

    def retrieveAssignments(self, request):
        C = Course.objects.get(courseId=request['courseId'])
        objlist = Assignment.objects.filter(course=C)
        return objlist


class Assignment(models.Model):
    # assignment code
    assignmentCode = models.CharField(max_length=10, primary_key=True)
    # link
    link = models.URLField(max_length=200)
    # course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # deadline
    deadline = models.DateField(auto_now=False, auto_now_add=True)
    # comments
    comments = models.TextField()
    # published_date
    publishedDate = models.DateField(auto_now=False, auto_now_add=True)

    objects = AssignmentManager()

    def __str__(self):
        return self.assignmentCode
