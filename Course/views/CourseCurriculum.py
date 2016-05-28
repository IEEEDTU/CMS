from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json


@csrf_exempt
@require_POST
def addCourseCurriculum(request):
    response_data = {}
    try:
        C = CourseCurriculum.objects.addCourseCurriculum(request.POST)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        data = serializers.serialize('json', [C, ])
        response_data["coursecurriculum"] = json.loads(data)
    return JsonResponse(response_data)


@csrf_exempt
@require_POST
def editCourseCurriculum(request):
    response_data = {}
    try:
        C = CourseCurriculum.objects.editCourseCurriculum(request.POST)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        data = serializers.serialize('json', [C, ])
        response_data["coursecurriculum"] = json.loads(data)
    return JsonResponse(response_data)


@csrf_exempt
@require_POST
def deleteCourseCurriculum(request):
    response_data = {}
    try:
        C = CourseCurriculum.objects.deleteCourseCurriculum(request.POST)
    except Exception as e:
        response_data['success'] = '0'
        response_data['exception'] = str(e)
    else:
        response_data['success'] = '1'
        data = serializers.serialize('json', [C, ])
        response_data["coursecurriculum"] = json.loads(data)
    return JsonResponse(response_data)


@csrf_exempt
@require_GET
def getCourseCurriculum(request):
    response_data = {}
    try:
        C = CourseCurriculum.objects.getCourseCurriculum(request.GET)
    except Exception as e:
        response_data["success"] = 0
        response_data['exception'] = str(e)
    else:
        response_data["success"] = 1
        data = serializers.serialize('json', [C.instructor, ])
        response_data["coursecurriculum"] = json.loads(data)

    return JsonResponse(response_data)


@csrf_exempt
@require_GET
def retrieveCourseCurriculum(request):
    response_data = {}
    try:
        C = CourseCurriculum.objects.retrieveCourseCurriculum(request.GET)
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
        response_data["coursecurriculum"] = json.loads(data)

    return JsonResponse(response_data)
