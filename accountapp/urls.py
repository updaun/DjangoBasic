# 21.06.30 accountapp urls
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # login
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # logout
    path('logout/', LogoutView.as_view(), name='logout'),
    # signup
    path('create/', AccountCreateView.as_view(), name='create')
]

