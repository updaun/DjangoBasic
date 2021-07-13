# 21.06.30 : Basic view
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import NewModel


def hello_world(request):
    # HttpResponse ALT+RETURN -> find import
    # 21.07.02
    #return HttpResponse('Hello World!')
    # 21.07.09 : rendering 분기
    #return render(request, 'accountapp/hello_world.html')
    if request.method == "POST":
        # 21.07.13 : input text
        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        # 새로고침하면 값이 추가되는 현상 방지
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})