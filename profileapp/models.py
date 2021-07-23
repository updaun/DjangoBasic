from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# models.CASCADE : 계정이 삭제되면 프로필도 삭제
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)

# 모델 생성 이후 migrate 해야 DB에 반영됨
# 명령어 python manage.py makemigrations  -> 바뀐 부분을 체크
# migrate 하려고 하면 에러가 발생 PIL 라이브러리 설치 ( pip install pillow )
# 명령어 python manage.py migrate -> 서버에 모델 반영