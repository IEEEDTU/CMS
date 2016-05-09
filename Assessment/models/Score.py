from django.db import models
from Profiler.models import Student
from Course.models import Course


class ScoreManager(models.Manager):
    def initScore(self, request):
        """ initialize the score """
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        C = Course.objects.get(courseId=request['courseId'])
        Sc = Score(
            student=S,
            course=C
        )
        Sc.save()
        return Sc

    def saveScore(self, request):
        """ save the score """
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        C = Course.objects.get(courseId=request['courseId'])
        Sc = Score.objects.get(student=S, course=C)
        Sc.sessMarks=request['sessMarks']
        Sc.endMarks=request['endMarks']
        Sc.marksObtained=request['sessMarks']+request['endMarks']
        Sc.creditsGained=request['creditsGained']
        Sc.save()
        return Sc

    def getScore(self, request):
        """ get score on the basis of student and course """
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        C = Course.objects.get(courseId=request['courseId'])
        Sc = Score.objects.get(student=S, course=C)
        return Sc

    def getScoresByStudent(self, request):
        """ get score according to student """
        S = Student.objects.get(dtuRegId=request['dtuRegId'])
        Sc = Score.objects.filter(student=S)
        return Sc

    def getScoresByCourse(self, request):
        """ get score according to course """
        C = Course.objects.get(courseId=request['courseId'])
        Sc = Score.objects.filter(course=C)
        return Sc


class Score(models.Model):
    # Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Sessional marks
    sessMarks = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    # End semester marks
    endMarks = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    # Total marks obtained
    marksObtained = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    # Total credits gained
    creditsGained = models.PositiveIntegerField(default=0)

    objects = ScoreManager()

    def __str__(self):
        return str(self.course) + " : " + str(self.marksObtained)
