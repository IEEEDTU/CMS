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
		response_data['exception'] = str(e)
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
		response_data['exception'] = str(e)
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
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ N, ])
		response_data["notice"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveLatestNotices(request):
	response_data = {}
	try:
		N = Notice.objects.retrieveLatestNotices(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', N)
		except Exception as e:
			data = serializers.serialize('json', [ N, ])
		response_data["notices"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveMoreNotices(request):
	response_data = {}
	try:
		N = Notice.objects.retrieveMoreNotices(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		global data
		try:
			data = serializers.serialize('json', N)
		except Exception as e:
			data = serializers.serialize('json', [ N, ])
		response_data["notices"] = json.loads(data)
	return JsonResponse(response_data)
