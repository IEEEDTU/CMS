from django.core import serializers
from django.http import HttpResponse,JsonResponse
from NewsFeed.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addEvent(request):
	response_data = {}
	try:
		E = Event.objects.addEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ E, ])
		response_data["event"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editEvent(request):
	response_data = {}
	try:
		E = Event.objects.editEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ E, ])
		response_data["event"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteEvent(request):
	response_data = {}
	try:
		E = Event.objects.deleteEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ E, ])
		response_data["event"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveLatestEvents(request):
	response_data = {}
	try:
		E = Event.objects.retrieveLatestEvents(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', E)
		except Exception as e:
			data = serializers.serialize('json', [ E, ])
		response_data["events"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveMoreEvents(request):
	response_data = {}
	try:
		E = Event.objects.retrieveMoreEvents(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', E)
		except Exception as e:
			data = serializers.serialize('json', [ E, ])
		response_data["events"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getEventById(request):
	response_data = {}
	try:
		E = Event.objects.getEventById(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', E)
		except Exception as e:
			data = serializers.serialize('json', [ E, ])
		response_data["events"] = json.loads(data)
	return JsonResponse(response_data)
