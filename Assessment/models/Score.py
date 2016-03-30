from django.db import models
from Profiler.models import Student
from Course.models import Course

class ScoreManager(models.Manager):
    def saveScore(self, request):
        S = Score(
            student = request['student'],
            course = request['course'],
            sessMarks = request['sessMarks'],
            endMarks = request['endMarks'],
            marksObtained = request['marksObtained'],
            creditsGained = request['creditsGained']
        )
        S.save()
        return S

    def getScore(self, request):
        S = Score.objects.get(student = request['student'], course = request['course'])
        #s = serializers.serialize('json', score)
        return S

class Score(models.Model):
	# Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    # Sessional marks
    sessMarks = models.DecimalField(decimal_places=1, max_digits=4)
    # End semester marks
    endMarks = models.DecimalField(decimal_places=1, max_digits=4)
    # Total marks obtained
    marksObtained = models.DecimalField(decimal_places=1, max_digits=4)
    # Total credits gained
    creditsGained = models.PositiveIntegerField()

    objects = ScoreManager()

    def __str__(self):
        return self.course + " : " + str(self.marksObtained)
