from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

#get Branch By COde
@csrf_exempt
@require_GET
def retrieveBranches(request):
	response_data = {}
	try:
		B = Branch.objects.retrieveBranches(request.GET)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', B)
		response_data['branches'] = json.loads(data)
	
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getBranchByCode(request):
	response_data = {}
	try:
		B = Branch.objects.getBranchByCode(request.GET)
	except Exception as e:
		response_data["success"] = 0
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [B, ])
		response_data["course"] = json.loads(data)

	return JsonResponse(response_data)