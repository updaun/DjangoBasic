# 21.06.30 : Basic view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel


def hello_world(request):
    # 21.07.21 : 로그인 인증
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))
    
# 회원가입 로직(기본 장고 제공)
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # class와 function의 호출이 다르다! 때문에 reverse_lazy 메서드를 사용하여 호출
    # success_url = reverse('accountapp:hello_world') # 작동 안됨
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = "accountapp/create.html"

# 계정 상세정보 로직(기본 장고 제공)
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = "accountapp/detail.html"

# 계정 정보 업데이트 로직(기본 장고 제공)
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = "accountapp/update.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

# 계정 삭제(기본 장고 제공)
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = "accountapp/delete.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))