from anyio import maybe_async
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import *

def login_page(request):
    return HttpResponse('NOT IMPLEMENTED.')

@csrf_exempt
def militants_page(request):
    if request.method == 'GET':
        militants = Militant.objects.all()
        serializer = MilitantSerializer(militants, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MilitantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def debts_page(request):
    if request.method == 'GET':
        militants = Militant.objects.all()
    return HttpResponse()

