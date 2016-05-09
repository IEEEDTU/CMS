from django.db import models
from Profiler.models import Student
from Course.models import *


class AssignmentManager(models.Manager):
    def __generateAssignmentCode__(self, request):
        """ generates assignment ID on the basis of course """
        code = request['courseId']
        C = Course.objects.getCourseById(request)
        A = Assignment.objects.filter(course=C).order_by('-assignmentCode')
        if A.exists() == True:
            lastCode = A[0].assignmentCode[-1:]
            code += chr(ord(lastCode) + 1)
        else:
            code += 'A'

        return code

    def addAssignment(self, request):
        """ add new assignment """
        C = Course.objects.get(courseId=request['courseId'])
        A = Assignment(
            assignmentCode=self.__generateAssignmentCode__(request),
            link=request['link'],
            course=C,
            deadline=request['deadline'],
            comments=request['comments'],
        )

        A.save()
        return A

    def editAssignment(self, request):
        """ edit the assignment """
        """ note: only deadline and comments are editable """
        A = Assignment.objects.get(assignmentCode=request['assignmentCode'])
        A.deadline = request['deadline']
        A.comments = request['comments']
        A.save()
        return A

    def deleteAssignment(self, request):
        """ delete an existing assignment """
        A = Assignment.objects.get(assignmentCode=request['assignmentCode'])
        A = A.delete()
        return A

    def getAssignmentByCode(self, request):
        """ get assignment on the basis of assignment code """
        A = Assignment.objects.get(assignmentCode=request['assignmentCode'])
        return A

    def getAssignmentsByCourse(self, request):
        """ get assignments on the basis of course """
        C = Course.objects.get(courseId=request['courseId'])
        A = Assignment.objects.filter(course=C)
        return A

    def retrieveAssignments(self, request):
        """ retrieve assignments on the basis of group """
        G = Group.objects.getGroupByIdAndCode(request)
        C = CourseGroup.objects.getCoursesByGroup(request)
        A = Assignment.objects.filter(course=C)
        return A


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
    comments = models.TextField(null=True)
    # published_date
    publishedDate = models.DateField(auto_now=False, auto_now_add=True)

    objects = AssignmentManager()

    def __str__(self):
        return self.assignmentCode
