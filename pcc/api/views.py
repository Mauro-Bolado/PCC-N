from django.shortcuts import render
from django.http import HttpResponse

from . import models

def login_page(request):
    return HttpResponse('NOT IMPLEMENTED')

def militants_page(request):
    militants = models.Militant.objects.all()
    HttpResponse(militants)
