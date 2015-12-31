from django.db import models

class CourseGroup(models.Model):
	# course = models.ForeignKey(
	# 	'Course',
	# 	on_delete = models.CASCADE,
	# )
	# group = models.ForeignKey(
	# 	'Group',
	# 	on_delete = models.CASCADE,
	# )
	# instructor = models.ForeignKey(
	# 	'Faculty',
	# 	on_delete = models.CASCADE,
	# )

	def __str__(self):
		 return "N/A"