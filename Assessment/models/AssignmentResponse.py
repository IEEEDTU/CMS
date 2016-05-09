from django.db import models
from Profiler.models import Student
from .Assignment import *


class AssignmentResponseManager(models.Manager):
    def addAssignmentResponse(self, request):
        """ add assignment response """
        A = Assignment.objects.getAssignmentByCode(request)
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        AR = AssignmentResponse(
            assignment=A,
            student=S,
            responseLink=request['responseLink'],
            status=1
        )
        AR.save()
        return AR

    def evaluateAssignmentResponse(self, request):
        """ saves evaluation grade of an assignment response """
        A = Assignment.objects.getAssignmentByCode(request)
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        AR = AssignmentResponse.objects.get(assignment=A, student=S)
        AR.grade = request['grade']
        AR.status = 2
        AR.save()
        return AR

    def deleteAssignmentResponse(self, request):
        """ deletes an assignment response """
        A = Assignment.objects.getAssignmentByCode(request)
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        AR = AssignmentResponse.objects.get(assignment=A, student=S)
        AR.delete()
        return AR

    def retrieveAssignmentResponsesByAssignment(self, request):
        """ retrieve student's assignment responses on the basis of assignment """
        """ note: assignment code is compulsory; submission date and status are optional fields """
        A = Assignment.objects.getAssignmentByCode(request)
        AR = AssignmentResponse.objects.filter(assignment=A)
        return AR

    def retrieveAssignmentResponsesByStudent(self, request):
        """ retrieve student's assignment responses on the basis of student """
        """ note: student's dtuRegId or roll no is compulsory; grade and status are optional fields """
        S = Student.objects.getStudentByRegIdOrRollNo(request)
        AR = AssignmentResponse.objects.filter(student=S)
        return AR


class AssignmentResponse(models.Model):
    NOT_SUBMITTED = 0
    SUBMITTED = 1
    EVALUATED = 2
    STATUS_CHOICES = ((NOT_SUBMITTED, 'Not Submitted'), (SUBMITTED, 'Submitted'), (EVALUATED, 'Evaluated'))

    # Assignment
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=False)
    # Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # Response link
    responseLink = models.URLField(max_length=200)
    # Grade
    grade = models.CharField(max_length=2, null=True)
    # submission date
    submissionDate = models.DateField(auto_now=False, auto_now_add=True)
    # status
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, null=False, blank=False, default=NOT_SUBMITTED)

    objects = AssignmentResponseManager()

    def __str__(self):
        return str(self.assignment) + str(self.student)
