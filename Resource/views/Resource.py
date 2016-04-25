from django.core import serializers
from django.http import HttpResponse,JsonResponse
from Resource.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addResource(request):
	response_data = {}
	try:
		R = Resource.objects.addResource(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ R, ])
		response_data["resource"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editResource(request):
	response_data = {}
	try:
		R = Resource.objects.editResource(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ R, ])
		response_data["resource"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteResource(request):
	response_data = {}
	try:
		R = Resource.objects.deleteResource(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ R, ])
		response_data["resource"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveResources(request):
	response_data = {}
	try:
		R = Resource.objects.retrieveResources(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', R)
		except Exception as e:
			data = serializers.serialize('json', [ R, ])
		response_data["resources"] = json.loads(data)
	return JsonResponse(response_data)
