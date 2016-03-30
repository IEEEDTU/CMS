from django.db import models
from django.core import serializers

class ScoreManager(models.Manager):
	def saveScore(self, req):
		# self.student = req['student']
		# self.course = req['course']
		self.sessMarks = req['sessMarks']
		self.endMarks = req['endMarks']
		self.marksObtained = req['marksObtained']
		self.creditsGained = req['creditsGained']
		
		score = Score(
			# self.student,
			# self.course,
			self.sessMarks,
			self.endMarks,
			self.marksObtained,
			self.creditsGained
		)
		score.save()
		return True
		
	# def getScore(self, req):
	# 	score = Score.objects.get(student = req['student'], course = req['course'])
	# 	s = serializers.serialize('json', score)
	# 	return s
		
	# def getScoreByStudent(self, student):
	# 	score = Score.objects.filter(student = student)
	# 	s = serializers.serialize('json', score)
	# 	return s 


class Score(models.Model):
	# student = models.ForeignKey(
	# 	'Student',
	# 	on_delete = models.CASCADE,
	# )
	# course = models.ForeignKey(
	# 	'Course',
	# 	on_delete = models.CASCADE,
	# )
	sessMarks = models.DecimalField(decimal_places = 1, max_digits = 4)
	endMarks = models.DecimalField(decimal_places = 1, max_digits = 4)	
	marksObtained = models.DecimalField(decimal_places = 1, max_digits = 4)	
	creditsGained = models.IntegerField()
	
	objects = ScoreManager()

	def __str__(self):
		return self.marksObtained