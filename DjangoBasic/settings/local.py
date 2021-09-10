from .base import *

# 21.07.02 read .env(secret key)
env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline() # 한 줄 읽기
    # 파일의 끝에 도달하면 종료
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=') # 첫 번째 '=' 찾아 인덱스 리턴
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value # env_list 딕셔너리 완성

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# 21.07.02 copy secret key and delete
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 21.08.11 : allow all ip
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
