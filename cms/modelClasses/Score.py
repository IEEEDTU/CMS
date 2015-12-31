from django.db import models

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

	def __str__(self):
		return self.marksObtained