from django.db import models
from django.core import serializers

class CourseManager(models.Manager):
	def addCourse(self, req):
		self.courseId = req['courseId']
		self.courseName = req['courseName']
		self.courseType = req['courseType']
		self.credits = req['credits']
		self.sessMaxMarks = req['sessMaxMarks']
		self.endMaxSemMarks = req['endMaxSemMarks']
		self.maxMarks = req['maxMarks'] 
		self.minPassingMarks = req['minPassingMarks']
		self.semester = req['semester']
		# self.degree = req['degree']
		# self.branch = req['branch']
		
		course = Course(self.courseId,
						self.courseName,
						self.courseType,
						self.credits, 
						self.sessMaxMarks, 
						self.endMaxSemMarks, 
						self.maxMarks, 
						self.minPassingMarks, 
						self.semester,
						# self.degree,
						# self.branch,
					)
		# do something with course
		course.save()
		return True
		
	def getCourseId(self, req):
		course = Course.objects.get(courseName = req['courseName'], semester = req['semester'],
									# degree = req['degree'],
									# branch = req['branch']
									)
		return course.courseId
	
	def getCourse(self, req):
		if req != {}:
			course = Course.objects.get(courseId = req['courseId'])
		else:
			course = Course.objects.all()
		s = serializers.serialize('json', course)
		return s
			
	def getCourseByType(self, req):
		course = Course.objects.filter(courseType = req['courseType'])
		s = serializers.serialize('json', course)
		return s
		
	def getCourseByBranch(self, req):
		course = Course.objects.filter(
			# branch = req['branch'],
			# degree = req['degree'],
			semester = req['semester']
		)
		s = serializers.serialize('json', course)
		return s
	
	def deleteCourse(self, req):
		if 'courseId' in req:
			course = Course.objects.filter(courseId = req['courseId'])
		else:
			course = Course.objects.filter(courseName = req['courseName'],
				# branch = req['branch'],
				# degree = req['degree'],
				semester = req['semester'])
		if course.delete():
			return True
		else:
			return False
		
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
	# degree = models.ForeignKey(
	# 	'Degree',
	# 	on_delete = models.CASCADE,
	# )
	# branch = models.ForeignKey(
	# 	'Branch',
	# 	on_delete = models.CASCADE,
	# )
	
	objects = CourseManager()
	
	def __str__(self):
		return self.courseId
		
req = {
# 	'courseId': 'SE-203',
# 	"courseName": "DS",
# 	"courseType": "Core",
# 	"credits": 4,
# 	"sessMaxMarks": 30,
# 	"endMaxSemMarks": 70,
# 	"maxMarks": 100,
# 	"minPassingMarks": 40,
	"semester": 3
}

# req = {
# 	'courseId': 'SE-203'
# }
	
#--> For testing
# print (Course.objects.getCourseByBranch(req))

# c = Course.objects.all()
# print (c)
# c.delete()

Course.objects.generateCourseId(req)