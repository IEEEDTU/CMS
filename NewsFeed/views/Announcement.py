from django.core import serializers
from django.http import HttpResponse,JsonResponse
from NewsFeed.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.addAnnouncement(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ A, ])
		response_data["announcement"] = json.loads(data)
	return JsonResponse(response_data)

def editAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.editAnnouncement(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ A, ])
		response_data["announcement"] = json.loads(data)
	return JsonResponse(response_data)

def deleteAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.deleteAnnouncement(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ A, ])
		response_data["announcement"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveLatestAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.retrieveLatestAnnouncement(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', A)
		except Exception as e:
			data = serializers.serialize('json', [ A, ])
		response_data["announcement"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveMoreAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.retrieveMoreAnnouncement(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', A)
		except Exception as e:
			data = serializers.serialize('json', [ A, ])
		response_data["announcement"] = json.loads(data)
	return JsonResponse(response_data)


