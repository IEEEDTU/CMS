from Course.models import *
from .Score import *


class ResultManager(models.Manager):
    def initResult(self, request):
        """ initialize the result and score of student """
        # initializing result
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        R = Result(
            student=S,
            semester=request['semester']
        )
        R.save()

        # initializing score
        C = Course.objects.filter(degree=S.degree, branch=S.branch, semester=request['semester'])
        for obj in C:
            Sc = Score(student=S, course=obj)
            Sc.save()

        return R

    def calculateResult(self, request):
        """ calculate the marks obtained from score class """
        # retrieving result object
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        R = Result.objects.get(student=S, semester=request['semester'])

        # calculating result
        C = Course.objects.filter(degree=S.degree, branch=S.branch, semester=request['semester'])

        totalScore = 0
        creditsGained = 0
        for obj in C:
            Sc = Score.objects.get(course=obj, student=S)
            totalScore += Sc.marksObtained
            creditsGained += Sc.creditsGained

        # saving the result
        R.totalScore=totalScore
        R.totalCredits=creditsGained
        R.save()
        return R

    def getResult(self, request):
        """ get the result on the basis of student and semester """
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        R = Result.objects.get(student=S, semester=request['semester'])
        return R

    def getResultsByStudent(self, request):
        """ get the result on the basis of student """
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        R = Result.objects.filter(student=S)
        return R

    def retrieveResults(self, request):
        """ retrieve result on the basis of degreeCode degreeType, branch and semester """
        """ note: all are compulsory fields except branch """
        S = Student.objects.retrieveStudents(request)
        R = Result.objects.filter(semester=request['semester'])
        R = R.filter(student__in = S)
        return R


class Result(models.Model):
    # Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # Semester
    semester = models.PositiveIntegerField()
    # Total credits gained
    totalCredits = models.PositiveIntegerField(default=0)
    # Total score obtained
    totalScore = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    # If locked=0 then result is hidden else visible
    locked = models.BooleanField(default=0)

    objects = ResultManager()

    def __str__(self):
        return str(self.student) + "_" + str(self.semester) + " : " + str(self.totalScore)
