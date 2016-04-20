from django.core import serializers
from django.http import HttpResponse
from Assessment.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
'''input is:  dtuRegId, courseId, sessMarks, endMarks, marksObtained, creditsGained'''
@csrf_exempt
@require_POST
def saveScore(request):
    S = Score.objects.saveScore(request)
    data = serializers.serialize('json', [S, ])
    print(data)
    return HttpResponse(data, content_type='application/json')