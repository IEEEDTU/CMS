from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addBranch(request):
	response_data = {}
	try:
		B = Branch.objects.addBranch(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ B, ])
		response_data["branch"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def editBranch(request):
	response_data = {}
	try:
		B = Branch.objects.editBranch(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ B, ])
		response_data["branch"] = json.loads(data)
	return JsonResponse(response_data)

@csrf_exempt
@require_POST
def deleteBranch(request):
	response_data = {}
	try:
		B = Branch.objects.deleteBranch(request.POST)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', [ B, ])
		response_data["branch"] = json.loads(data)
	return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveBranches(request):
	response_data = {}
	try:
		B = Branch.objects.retrieveBranches(request.GET)
	except Exception as e:
		response_data['success'] = '0'
		response_data['exception'] = str(e)
	else :
		response_data['success'] = '1'
		try:
			data = serializers.serialize('json', B)
		except Exception as e:
			data = serializers.serialize('json', [ B, ])
		response_data["branches"] = json.loads(data)
	
	return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getBranchByCode(request):
	response_data = {}
	try:
		B = Branch.objects.getBranchByCode(request.GET)
	except Exception as e:
		response_data["success"] = 0
		response_data['exception'] = str(e)
	else:
		response_data["success"] = 1
		data = serializers.serialize('json', [B, ])
		response_data["course"] = json.loads(data)

	return JsonResponse(response_data)
