from django.db import models

class Course(models.Model):
	courseId = models.CharField(max_length=10, primary_key=True)
	courseName = models.CharField(max_length=100, blank=False, null=False)
	courseType = models.CharField(max_length=10, blank=False, null=False)
	credits = models.IntegerField()
	sessMaxMarks = models.DecimalField(decimal_places = 1, max_digits = 4)
	endMaxSemMarks = models.DecimalField(decimal_places = 1, max_digits = 4)
	maxMarks = models.DecimalField(decimal_places = 1, max_digits = 4)
	minPassingMarks = models.DecimalField(decimal_places = 1, max_digits = 4)
	semester = models.IntegerField()
	# branch = models.ForeignKey(
	# 	'branch',
	# 	on_delete = models.CASCADE,
	# )
	
	def __str__(self):
		return self.courseId
		
	@classmethod
	def create(cls, courseId, courseName, courseType, credits, sessMaxMarks, endMaxSemMarks, maxMarks, minPassingMarks, semester):
		course = cls(courseId = courseId, courseName = courseName, courseType = courseType, credits = credits,
						sessMaxMarks = sessMaxMarks, endMaxSemMarks = endMaxSemMarks, maxMarks = maxMarks, 
						minPassingMarks = minPassingMarks, semester = semester)
		# do something with course
		course.save()
		return course
		
# course = Course.create("SE-203", "DS", "Core", 4, 30, 70, 100, 40, 3) --> For testing

		
		
	
	