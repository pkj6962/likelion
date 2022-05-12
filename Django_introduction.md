장고프로젝트의 시작
=================

    python3 -m venv myvenv 

명령어를 통해 가상환경을 설치해주었다. 가상환경은 오직 어떤 프로젝트만을 위한 세팅을 하는 것으로, 다른 프로젝트에 의도하지 않은 종속성 문제를 일으키지 않는 것을 돕는다. 

위 명령어를 통해 설치된 myvenv 폴더 안에 activate 라는 실행파일을 source 명령어를 통해 실행하면 셸에 (myvenv)라는 문구가 기본적으로 표시된다. 

    pip install django

로 장고를 설치해주고, 

    django-admin startporject myproject

로 프로젝트 파일을 생성해주었다. 

이 프로젝트 파일에는 몇 가지 기본 파이썬 파일이 내장되어 있다.

    __init__.py

이러한 이름을 가진 파일은 이것이 위치한 곳이 '패키지'라는 것을 알려주는 약속된 이름의 파일이다.
내용은 없다. 

    asgi.py

    settings.py

manage.py로 앱을 만들고 나면, settins.py 안에 installed_apps 라는 리스트에 해당 앱을 추가해주어야 한다. 

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dashboard'
]
```

    urls.py

우리 웹페이지의 url을 관리하는 파일 

    wsgi.py

    manage.py
중요!
1. 서버 켜기 
    python manage.py runserver 
포트번호 8000에 로컬 서버가 생성된다. 

2. Application(장고의 작은 구성 단위) 만들기
게시판, 장바구니, 결제 기능 앱을 각각 만들어 쇼핑몰 프로젝트에 병합하는게 더 효율적(divide and conquer!)

    python django manage.py startapp 앱이름 

또 새로운 폴더가 생성된다. 

폴더에는 model.py, view.py, test.py 라는 파일이 있다. 즉 MTV 패턴으로 개발을 할 수 있는 것이다. 


기능 단위로 각 폴더에서 따로따로 뚝닥뚝닥 개발하면 된다. 


3. Database 초기화 및 변경사항 반영(migrate)



4. 관리자 계정 만들기 



