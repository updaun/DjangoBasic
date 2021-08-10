"""DjangoBasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 21.07.23 python manage.py createsuperuser
    path('admin/', admin.site.urls),
    # 21.06.30 add account path
    path('accounts/', include('accountapp.urls')),
    # 21.07.23 add profile path
    path('profiles/', include('profileapp.urls')),
    # 21.07.30 add article path
    path('articles/', include('articleapp.urls')),
    # 21.08.10 add comment path
    path('comments/', include('commentapp.urls')),
    # 21.07.28 image load
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
