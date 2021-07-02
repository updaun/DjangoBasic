# 21.06.30 : Basic view
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    # HttpResponse ALT+RETURN -> find import
    # 21.07.02
    #return HttpResponse('Hello World!')
    return render(request, 'accountapp/hello_world.html')