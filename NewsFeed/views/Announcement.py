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
	else :
		response_data['success'] = '1'
		response_data['announcement'] = A
	return JsonResponse(response_data)

def editAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.editAnnouncement(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['announcement'] = A
	return JsonResponse(response_data)

def deleteAnnouncement(request):
	response_data = {}
	try:
		A = Announcement.objects.deleteAnnouncement(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['announcement'] = A
	return JsonResponse(response_data)

