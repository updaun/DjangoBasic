# 21.06.30 : Basic view
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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

        # database 모두 보기
        data_list = NewModel.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={'data_list':data_list})
    else:
        data_list = NewModel.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})