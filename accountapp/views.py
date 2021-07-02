# 21.06.30 : Basic view
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    # HttpResponse ALT+RETURN -> find import
    return HttpResponse('Hello World!')