from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json


@csrf_exempt
@require_GET
def retrieveBatches(request):
	response_data = {}
	try:
		B = Batch.objects.retrieveBatches(request.GET)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', B)
		response_data['batches'] = json.loads(data)
	
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getBatchById(request):
	response_data = {}
	try:
		B = Batch.objects.getBatchById(request.GET)
	except Exception as e:
		response_data["success"] = 0
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [B, ])
		response_data["batches"] = json.loads(data)

	return JsonResponse(response_data)
