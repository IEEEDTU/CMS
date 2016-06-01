from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Assessment.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_GET
def getAssignmentByCode(request):
    response_data = {}
    try:
        C = Assignment.objects.getAssignmentByCode(request.GET)
    except Exception as e:
        response_data["success"] = 0
        response_data['exception'] = str(e)
    else:
        response_data["success"] = 1
        data = serializers.serialize('json', [C, ])
        response_data["assignment"] = json.loads(data)

    return JsonResponse(response_data)

@csrf_exempt
@require_GET
def getAssignmentsByCourse(request):
    print (request)
    response_data = {}
    try:
        C = Assignment.objects.getAssignmentsByCourse(request.GET)
    except Exception as e:
        response_data["success"] = 0
        response_data['exception'] = str(e)
    else:
        response_data["success"] = 1
        data = serializers.serialize('json', [C, ])
        response_data["assignment"] = json.loads(data)

    return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveAssignmentByBranch(request):
    response_data = {}
    try:
        C = Assignment.objects.filter(assignmentCode__contains="SE")
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        global data
        try:
            data = serializers.serialize('json', C)
        except Exception as e:
            data = serializers.serialize('json', [C, ])
        response_data["assignment"] = json.loads(data)

    return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveAssignmentResponses(request):
    response_data = {}
    try:
        C = AssignmentResponse.objects.retrieveAssignmentResponsesByStudent(request.GET)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        global data
        try:
            data = serializers.serialize('json', C)
        except Exception as e:
            data = serializers.serialize('json', [C, ])
        response_data["assignment"] = json.loads(data)

    return JsonResponse(response_data)

@csrf_exempt
@require_GET
def retrieveAssignments(request):
    response_data = {}
    try:
        C = Assignment.objects.retrieveAssignments(request.GET)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        global data
        try:
            data = serializers.serialize('json', C)
        except Exception as e:
            data = serializers.serialize('json', [C, ])
        response_data["assignment"] = json.loads(data)

    return JsonResponse(response_data)
