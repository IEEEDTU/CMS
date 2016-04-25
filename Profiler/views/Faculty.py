from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Profiler.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addFaculty(request):
	response_data = {}
	try:
		F = Faculty.objects.addFaculty(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ F, ])
		response_data["faculty"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editFaculty(request):
	response_data = {}
	try:
		F = Faculty.objects.editFaculty(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ F, ])
		response_data["faculty"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteFaculty(request):
	response_data = {}
	try:
		F = Faculty.objects.deleteFaculty(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ F, ])
		response_data["faculty"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getFacultyById(request):
	response_data = {}
	try:
		F = Faculty.objects.getFacultyById(request.GET)
	except Exception as e:
		response_data["success"] = 0
		response_data['exception'] = str(e)
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [ F, ])
		response_data["faculty"] = json.loads(data)

	return JsonResponse(response_data)

