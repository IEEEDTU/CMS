from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addDegree(request):
	response_data = {}
	try:
		D = Degree.objects.addDegree(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data["degree"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editDegree(request):
	response_data = {}
	try:
		D = Degree.objects.editDegree(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data["degree"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteDegree(request):
	response_data = {}
	try:
		D = Degree.objects.deleteDegree(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data["degree"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveDegrees(request):
	response_data = {}
	try:
		D = Degree.objects.retrieveDegrees(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		try:
			data = serializers.serialize('json', D)
		except Exception as e:
			data = serializers.serialize('json', [ D, ])
		response_data["degrees"] = json.loads(data)
	
	return JsonResponse(response_data)

	
@csrf_exempt
@require_GET
def getDegreeByCodeAndType(request):
	response_data = {}
	try:
		D = Degree.objects.getCourseById(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ D, ])
		response_data['degree'] = json.loads(data)
	
	return JsonResponse(response_data)
	
