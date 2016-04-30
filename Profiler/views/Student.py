from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Profiler.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addStudent(request):
	response_data = {}
	try:
		S = Student.objects.addStudent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ S, ])
		response_data["student"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editStudent(request):
	response_data = {}
	try:
		S = Student.objects.editStudent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ S, ])
		response_data["student"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteStudent(request):
	response_data = {}
	try:
		S = Student.objects.deleteStudent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ S, ])
		response_data["student"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getStudentByRollNo(request):
	response_data = {}
	try:
		S = Student.objects.getStudentByRollNo(request.GET)
	except Exception as e:
		response_data["success"] = 0
		response_data['exception'] = str(e)
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [ S, ])
		response_data["student"] = json.loads(data)
		del response_data["student"][0]["fields"]["password"]

	return JsonResponse(response_data)


"""
def searchStudent(request):
    

def getStudentsByName(request):


def getStudentsByDegree(request):


def getStudentsByBranch(request):

"""
