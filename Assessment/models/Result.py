from django.db import models
from Profiler.models import Student
from Course.models import *
from .Score import *


class ResultManager(models.Manager):
    # This function is used to calculate the marks obtained from score class
    def calculateResult(self, request):
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        D = Degree.objects.get(degreeCode=request['degreeCode'], degreeType=request["degreeType"]),
        B = Branch.objects.get(branchCode=request['branchCode'])
        C = Course.objects.filter(degree=D, branch=B, semester=request['semester'])

        totalScore = 0
        creditsGained = 0
        for obj in C:
            Sc = Score.objects.get(Course=obj, Student=S)
            totalScore += Sc.marksObtained
            creditsGained += Sc.creditsGained
        R = Result(
            student=S,
            semester=request['semester'],
            totalCredits=creditsGained,
            totalScore=totalScore
        )
        R.save()
        return R

    # This function will receive dtuRegId and semester to get the result of the required student of that particular sem
    def getResult(self, request):
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        R = Result.objects.get(student=S, semester=request['semester'])
        return R


class Result(models.Model):
    # Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # Semester
    semester = models.PositiveIntegerField()
    # Total credits gained
    totalCredits = models.PositiveIntegerField()
    # Total score obtained
    totalScore = models.DecimalField(decimal_places=1, max_digits=4)
    # If locked=0 then result is hidden else visible
    locked = models.BooleanField(default=0)

    objects = ResultManager()

    def __str__(self):
        return str(self.student) + "_" + str(self.semester) + " : " + str(self.totalScore)
