from django.db import models

# Create your models here.
# 21.07.09 : add model
# models.Model 상속받음, django의 기본 모델
# 명령어 python manage.py makemigrations  -> 바뀐 부분을 체크
# 명령어 python manage.py migrate -> 서버에 모델 반영
class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False)

