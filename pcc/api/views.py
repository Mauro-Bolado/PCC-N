# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from .serializers import *
# from .models import *

# def login_page(request):
#     return HttpResponse('NOT IMPLEMENTED.')

# @csrf_exempt
# def militants_page(request):
#     if request.method == 'GET':
#         militants = Militant.objects.all()
#         serializer = MilitantSerializer(militants, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MilitantSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def militants_detail(request, pk):
#     try:
#         militant = Militant.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=404)  
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)  
#         serializer = MilitantSerializer(militant, data=data)
#         if(serializer.is_valid()):  
#             serializer.save() 
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         militant.delete() 
#         return HttpResponse(status=204) 

# @csrf_exempt
# def debts_page(request):
#     if request.method == 'GET':
#         militants = Militant.objects.all()
#         serializer = DebtsSerializer.serialize(militants, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         militants = MilitantSerializer(data=data)
#         serializer = DebtsSerializer.serialize(militants, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.data, status=400)

# @csrf_exempt
# def core_page(request):
#     if request.method == 'GET':
#         cores = Core.objects.all()
#         serializer = CoreSerializer(cores, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CoreSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def core_detail(request, pk):
#     try:
#         core = Militant.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=404)  
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)  
#         serializer = MilitantSerializer(core, data=data)
#         if(serializer.is_valid()):  
#             serializer.save() 
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         core.delete() 
#         return HttpResponse(status=204)

# @csrf_exempt
# def adress_page(request):
#     if request.method == 'GET':
#         addresses = Address.objects.all()
#         serializer = AddressSerializer(addresses, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AddressSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     else:
#         JsonResponse({'error': '{} method not implemented'.format(request.method)})

# @csrf_exempt
# def address_detail(request, pk):
#     try:
#         adress = Address.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=404)
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)  
#         serializer = AddressSerializer(adress, data=data)
#         if(serializer.is_valid()):  
#             serializer.save() 
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         adress.delete() 
#         return HttpResponse(status=204)

from operator import imod
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import Response

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, Group, Permission

import json

from .serializers import *
from .models import Address, Militant, PaymentNorm, Core, Payment


class Address_APIView(APIView):
    def get_queryset(self):
        return Address.objects.none

    def post(self, request, format=None):
        serializer = AddressSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Core_APIView(APIView):
    def get_queryset(self):
        return Core.objects.all()

    def get(self, request, format=None, *args, **kwargs):
        cores = self.get_queryset()
        serializer_cores = CoreSerializer(cores, many=True)
        return JsonResponse(serializer_cores.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = CoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Core_APIView_Detail(APIView):
    def get_queryset(self):
        return Core.objects.none

    def get(self, request, pk, format=None):
        core = get_object_or_404(Core, pk=pk)
        serializer = CoreSerializer(core)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def put(self, request, pk, format=None):
        core = get_object_or_404(Core, pk=pk)
        serializer = CoreSerializer(data=request.data)
        if serializer.is_valid():
            core.delete()
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk, format=None):
        core = get_object_or_404(Core, pk=pk)
        core.delete()
        serializer = CoreSerializer(core)
        return HttpResponse(serializer.data, status=status.HTTP_204_NO_CONTENT, safe=False)


class Militant_APIView(APIView):
    def get_queryset(self):
        militant = Militant.objects.all()
        return militant

    def get(self, request, format=None, *args, **kwargs):
        militant = self.get_queryset()
        serializer = MilitantSerializer(militant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = MilitantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Militant_APIView_Detail(APIView):
    def get_queryset(self):
        militant = Militant.objects.none
        return militant

    def get(self, request, pk, format=None):
        militant = get_object_or_404(Militant, pk=pk)
        serializer = MilitantSerializer(militant)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def put(self, request, pk, format=None):
        militant = get_object_or_404(Militant, pk)
        serializer = MilitantDeclarationsSerializer(
            militant, data=request.data)
        if serializer.is_valid():
            militant.delete()
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk, format=None):
        militant = get_object_or_404(Militant, pk)
        militant.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT, safe=False)


class DeclarationDate_APIView(APIView):
    def get_queryset(self):
        return DeclarationDate.objects.all()

    def get(self, request, format=None):
        serializer = DeclarationDateSerializer(
            self.get_queryset(), many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = DeclarationDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class PaymentDeclaration_APIView(APIView):
    def get_queryset(self):
        return PaymentDeclaration.objects.none

    def post(self, request, format=None):
        serializer = PaymentDeclarationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class PaymentDate_APIView(APIView):
    def get_queryset(self):
        return PaymentDate.objects.all()

    def get(self, request, format=None):
        serializer = PaymentDateSerializer(
            self.get_queryset(), many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = PaymentDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Payment_APIView(APIView):
    def get_queryset(self):
        return Payment.objects.all()

    def get(self, request, format=None):
        payment = self.get_queryset()
        serializer = PaymentSerializer(payment)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Debts_APIView(APIView):
    def get_queryset(self):
        return Militant.objects.all()

    def get(self, request, format=None):
        arrears = MilitantDebtsSerializer.serialize(self.get_queryset(), True)
        return JsonResponse(arrears, status=status.HTTP_200_OK, safe=False)


class Debts_APIViews_Detail(APIView):
    def get_queryset(self):
        return Militant.objects.none

    def get(self, request, pk, format=None):
        militant = Militant.objects.filter(pk=pk)
        if len(militant) != 0:
            if len(militant[0].arrears_fees()) == 0:
                body = {'message': 'Militant it is clean'}
                return HttpResponse(json.dumps(body), status=status.HTTP_404_NOT_FOUND, content_type='application/json')
            else:
                serializer = MilitantDebtsSerializer.serialize(militant)
                return JsonResponse(serializer, status=status.HTTP_200_OK, safe=False)
        else:
            body = {'error': 'Militant do not exist'}
            return HttpResponse(json.dumps(body), status=status.HTTP_404_NOT_FOUND, content_type='application/json')


class User_APIView(APIView):
    def get_queryset(self):
        return User.objects.all()

    def get(self, request, format=None):
        serializer = UserSerializer(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = User(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Group_APIView(APIView):
    def get_queryset(self):
        return Group.objects.all()

    def get(self, request, format=None):
        serializer = UserSerializer(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = User(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Group_APIViews_Details(APIView):
    def get_queryset(self):
        return [Permission.objects.all(), Group.objects.none]

    def put(self, request, pk, format=None):
        auth_group = get_object_or_404(Group, pk=pk)
        permissions = request.PUT['permissions']
        auth_group.permissions.add(permissions)

    def get(self, request, format=None):
        serializer = GroupSerializer(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, safe=False)
