from django.core import serializers
from django.http import HttpResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# input : courseId, courseName, courseType, credits, sessMaxMarks, endMaxSemMarks, maxMarks, minPassingMarks, semester, degreeCode, degreeType, branchCode
@csrf_exempt
@require_POST
def addCourse(request):
	C = Course.objects.addCourse(request.POST)
	data = serializers.serialize('json', [ C, ])
	print(data)
	return HttpResponse(data, content_type='application/json')
	