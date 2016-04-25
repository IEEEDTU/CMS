from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addDepartment(request):
	response_data = {}
	try:
		D = Department.objects.addDepartment(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data["department"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editDepartment(request):
	response_data = {}
	try:
		D = Department.objects.editDepartment(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data["department"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteDepartment(request):
	response_data = {}
	try:
		D = Department.objects.deleteDepartment(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data["department"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveDepartments(request):
	response_data = {}
	try:
		D = Department.objects.retrieveDepartments(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', D)
		except Exception as e:
			data = serializers.serialize('json', [ D, ])
		response_data["departments"] = json.loads(data)
	
	return JsonResponse(response_data)
