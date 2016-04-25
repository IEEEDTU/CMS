from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from Profiler.models import Faculty
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addCourseGroup(request):
	response_data = {}
	try:
		C = CourseGroup.objects.addCourseGroup(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ C, ])
		response_data["coursegroup"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editCourseGroup(request):
	response_data = {}
	try:
		C = CourseGroup.objects.editCourseGroup(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ C, ])
		response_data["coursegroup"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteCourseGroup(request):
	response_data = {}
	try:
		C = CourseGroup.objects.deleteCourseGroup(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ C, ])
		response_data["coursegroup"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getInstructorDetails(request):
	response_data = {}
	try:
		C = CourseGroup.objects.getCourseGroupById(request.GET)
		I = Faculty.objects.get(dtuRegId = C.instructor)
	except Exception as e:
		response_data["success"] = 0
		response_data['exception'] = str(e)
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [I, ])
		response_data["course"] = json.loads(data)

	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveCourseGroups(request):
	response_data = {}
	try:
		C = CourseGroup.objects.retrieveCourseGroups(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', C)
		except Exception as e:
			data = serializers.serialize('json', [ C, ])
		response_data["coursegroups"] = json.loads(data)
	
	return JsonResponse(response_data)
