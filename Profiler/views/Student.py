from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Profiler.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json
from datetime import datetime

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

@csrf_exempt
@require_GET
def retrieveProjects(request):
    response_data = {}
    try:
        P = Project.objects.retrieveProjects(request.GET)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        global data
        try:
            data = serializers.serialize('json', P)
        except Exception as e:
            data = serializers.serialize('json', [P, ])
        response_data["projects"] = json.loads(data)

    return JsonResponse(response_data)

@csrf_exempt
@require_POST
def addProject(request):
	response_data = {}
	try:
		#startDate = datetime.strptime(request.POST['startDate'][:-27], '%a %b %d %Y %H:%M:%S %Z')
		#request.POST['startDate'] = str(startDate.year) + "-" + str(startDate.month) + "-" + str(startDate.day)

		#endDate = datetime.strptime(request.POST['endDate'][:-27], '%a %b %d %Y %H:%M:%S %Z')
		#request.POST['endDate'] = str(endDate.year) + "-" + str(endDate.month) + "-" + str(endDate.day)

		print(request.POST['startDate'])
		print(request.POST['endDate'])
		P = Project.objects.addProject(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ P, ])
		response_data["student"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveSkills(request):
    response_data = {}
    try:
        P = Skill.objects.retrieveSkills(request.GET)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        global data
        try:
            data = serializers.serialize('json', P)
        except Exception as e:
            data = serializers.serialize('json', [P, ])
        response_data["skills"] = json.loads(data)

    return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveFields(request):
    response_data = {}
    try:
        P = Field.objects.retrieveFields(request.GET)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        global data
        try:
            data = serializers.serialize('json', P)
        except Exception as e:
            data = serializers.serialize('json', [P, ])
        response_data["fields"] = json.loads(data)

    return JsonResponse(response_data)



@csrf_exempt
@require_POST
def addSkill(request):
	response_data = {}
	try:
		S = Skill.objects.addSkill(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ S, ])
		response_data["skill"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def addField(request):
	response_data = {}
	try:
		S = Field.objects.addField(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ S, ])
		response_data["field"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteSkill(request):
	response_data = {}
	try:
		S = Skill.objects.deleteSkill(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteField(request):
	response_data = {}
	try:
		S = Field.objects.deleteField(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
	return JsonResponse(response_data)

"""
def searchStudent(request):
    

def getStudentsByName(request):


def getStudentsByDegree(request):


def getStudentsByBranch(request):

"""
