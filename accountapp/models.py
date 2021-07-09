from django.db import models

# Create your models here.
# 21.07.09 : add model
# models.Model 상속받음, django의 기본 모델
# 명령어 python manage.py makemigrations
# 명령어 python manage.py migrate
class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False)

