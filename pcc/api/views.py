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
def militants_detail(request, pk):
    try:
        militant = Militant.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if request.method == 'PUT':
        data = JSONParser().parse(request)  
        serializer = MilitantSerializer(militant, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        militant.delete() 
        return HttpResponse(status=204) 

@csrf_exempt
def debts_page(request):
    if request.method == 'GET':
        militants = Militant.objects.all()
        serializer = DebtsSerializer.serialize(militants, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        militants = MilitantSerializer(data=data)
        serializer = DebtsSerializer.serialize(militants, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def core_page(request):
    if request.method == 'GET':
        cores = Core.objects.all()
        serializer = CoreSerializer(cores, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def core_detail(request, pk):
    try:
        core = Militant.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if request.method == 'PUT':
        data = JSONParser().parse(request)  
        serializer = MilitantSerializer(core, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        core.delete() 
        return HttpResponse(status=204)

@csrf_exempt
def adress_page(request):
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def address_detail(request, pk):
    try:
        adress = Address.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if request.method == 'PUT':
        data = JSONParser().parse(request)  
        serializer = AddressSerializer(adress, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        adress.delete() 
        return HttpResponse(status=204)