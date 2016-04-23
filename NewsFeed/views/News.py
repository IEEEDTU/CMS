from django.core import serializers
from django.http import HttpResponse,JsonResponse
from NewsFeed.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addNews(request):
	response_data = {}
	try:
		N = News.objects.addNews(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ N, ])
		response_data["news"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editNews(request):
	response_data = {}
	try:
		N = News.objects.editNews(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['news'] = N
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteNews(request):
	response_data = {}
	try:
		N = News.objects.deleteNews(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['news'] = N
	return JsonResponse(response_data)


@csrf_exempt
@require_POST
def retrieveLatestNews(request):
	response_data = {}
	try:
		N = News.objects.retrieveLatestNews(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['news'] = N
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def retrieveMoreNews(request):
	response_data = {}
	try:
		N = News.objects.retrieveMoreNews(request.POST)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		response_data['news'] = N
	return JsonResponse(response_data)
