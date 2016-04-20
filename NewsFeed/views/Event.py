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
	else :
		response_data['success'] = '1'
		response_data['event'] = N
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editEvent(request):
	response_data = {}
	try:
		E = Event.objects.editEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['event'] = E
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteEvent(request):
	response_data = {}
	try:
		E = Event.objects.deleteEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['event'] = E
	return JsonResponse(response_data)


@csrf_exempt
@require_POST
def retrieveLatestEvent(request):
	response_data = {}
	try:
		E = Event.objects.retrieveLatestEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['event'] = E
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def retrieveMoreEvent(request):
	response_data = {}
	try:
		E = Event.objects.retrieveMoreEvent(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['event'] = E
	return JsonResponse(response_data)
