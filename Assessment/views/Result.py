from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Assessment.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_GET
def getResultsByStudent(request):
    response_data = {}
    try:
        C = Result.objects.getResultsByStudent(request.GET)
        print (C)
    except Exception as e:
        response_data["success"] = 0
        response_data['exception'] = str(e)
    else:
        response_data["success"] = 1
        data = serializers.serialize('json', [C, ])
        response_data["result"] = json.loads(data)

    return JsonResponse(response_data)
