from django.db import models

class Result(models.Model):
	# student = models.ForeignKey(
	# 	'Student',
	# 	on_delete = models.CASCADE,
	# )
	semester = models.IntegerField()
	totalCredits = models.IntegerField()
	totalScore = models.DecimalField(decimal_places = 1, max_digits = 4)	
	
	def __str__(self):
		return self.totalScore