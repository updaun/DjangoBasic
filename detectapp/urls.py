from django.urls import path

from . import views

app_name = 'detectapp'

urlpatterns = [
    path('holistic/', views.holistic, name='holistic'),
    path('detectme/', views.detectme, name='detectme')
]