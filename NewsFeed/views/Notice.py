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
		data = serializers.serialize('json', [ N, ])
		response_data["notice"] = json.loads(data)
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
		data = serializers.serialize('json', [ N, ])
		response_data["notice"] = json.loads(data)
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
		data = serializers.serialize('json', [ N, ])
		response_data["notice"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveLatestNotice(request):
	response_data = {}
	try:
		N = Notice.objects.retrieveLatestNotice(request.GET)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', N)
		except Exception as e:
			data = serializers.serialize('json', [ N, ])
		response_data["notice"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveMoreNotice(request):
	response_data = {}
	try:
		N = Notice.objects.retrieveMoreNotice(request.GET)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', N)
		except Exception as e:
			data = serializers.serialize('json', [ N, ])
		response_data["notice"] = json.loads(data)
	return JsonResponse(response_data)
