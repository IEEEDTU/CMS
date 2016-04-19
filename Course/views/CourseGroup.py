from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json


@csrf_exempt
@require_GET
def retrieveCourseGroups(request):
	response_data = {}
	try:
		C = CourseGroup.objects.retrieveCourseGroups(request.GET)
	except Exception as e:
		response_data['success'] = '0'
	else :
		response_data['success'] = '1'
		data = serializers.serialize('json', C)
		response_data['branches'] = json.loads(data)
	
	return JsonResponse(response_data)

