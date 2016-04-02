from django.core import serializers
from django.http import HttpResponse
from Course.models import *

# input : courseId, courseName, courseType, credits, sessMaxMarks, endMaxSemMarks, maxMarks, minPassingMarks, semester, degreeCode, degreeType, branchCode
def addCourse(request):
	C = Course.objects.addCourse(request)
	data = serializers.serialize('json', [ C, ])
	print(data)
	return HttpResponse(data, content_type='application/json')
	