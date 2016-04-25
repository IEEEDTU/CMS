from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addGroup(request):
	response_data = {}
	try:
		G = Group.objects.addGroup(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ G, ])
		response_data["group"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editGroup(request):
	response_data = {}
	try:
		G = Group.objects.editGroup(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ G, ])
		response_data["group"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteGroup(request):
	response_data = {}
	try:
		G = Group.objects.deleteGroup(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ G, ])
		response_data["group"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveGroups(request):
	response_data = {}
	try:
		G = Group.objects.retrieveGroups(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', G)
		except Exception as e:
			data = serializers.serialize('json', [ G, ])
		response_data["groups"] = json.loads(data)
	
	return JsonResponse(response_data)
