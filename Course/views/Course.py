from django.core import serializers
from django.http import HttpResponse,JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

# input : courseId, courseName, courseType, credits, sessMaxMarks, endMaxSemMarks, maxMarks, minPassingMarks, semester, degreeCode, degreeType, branchCode
@csrf_exempt
@require_POST
def addCourse(request):
	response_data = {}
	try:
		C = Course.objects.addCourse(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['course'] = C
	# data = serializers.serialize('json', [ C, ])
	# print(data)
	# return HttpResponse(data, content_type='application/json')
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveCourses(request):
	response_data = {}
	list = []
	try:	
		C = Course.objects.retrieveCourses(request.GET)
		print(C)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		#for obj in C:
			#dic = {'courseId' : obj.courseId, 'courseName' :obj.courseName}
			#list.append(dic)
		#response_data['courses'] = list
		data = serializers.serialize('json', C)
		response_data["courses"] = json.loads(data)
		
	return JsonResponse(response_data)
	
@csrf_exempt
@require_GET
def getCourseById(request):
	response_data = {}
	try:
		C = Course.objects.getCourseById(request.GET)
	except Exception as e:
		response_data["success"] = 0
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [C, ])
		response_data["course"] = json.loads(data)

	return JsonResponse(response_data)
	# data = serializers.serialize('json', [C, ])
	# return HttpResponse(data, content_type='application/json')
	
