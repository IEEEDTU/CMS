from django.core import serializers
from django.http import HttpResponse,JsonResponse
from NewsFeed.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addNotice(request):
	response_data = {}
	try:
		N = Notice.objects.addNotice(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['notice'] = N
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editNotice(request):
	response_data = {}
	try:
		N = Notice.objects.editNotice(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['notice'] = N
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteNotice(request):
	response_data = {}
	try:
		N = Notice.objects.deleteNotice(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['notice'] = N
	return JsonResponse(response_data)


@csrf_exempt
@require_POST
def retrieveLatestNotice(request):
	response_data = {}
	try:
		N = Notice.objects.retrieveLatestNotice(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['notice'] = N
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def retrieveMoreNotice(request):
	response_data = {}
	try:
		N = Notice.objects.retrieveMoreNotice(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['notice'] = N
	return JsonResponse(response_data)
