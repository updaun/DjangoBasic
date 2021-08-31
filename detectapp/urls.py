from django.urls import path

from . import views

app_name = 'detectapp'

urlpatterns = [
    path('camview/', views.camview, name='camview'),
    path('opencamera/', views.opencamera, name='opencamera'),
    path('holistic/', views.holistic, name='holistic'),
    path('detectme/', views.detectme, name='detectme')
]