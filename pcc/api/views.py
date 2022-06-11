from django.shortcuts import render
from django.http import HttpResponse

from . import models

def login_page(request):
    return HttpResponse('NOT IMPLEMENTED.')

def militants_page(request):
    militants = models.Militant.objects.all()
    if not len(militants) > 0:
        return HttpResponse('NO ELEMENTS TO SEND.')
    else:
        return HttpResponse(militants)
