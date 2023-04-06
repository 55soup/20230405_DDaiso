# DDaiso

- **프로젝트이름/urls.py -> 앱이름/urls.py -> 앱이름/views.py -> 앱이름/models.py -> templates/앱이름/HTML파일이름.html**
- admin.py: 관리자 사이트
- form.py: 입력폼 사이트
- 개발 순서: modles.py, views.py, urls.py, templates

---
1. startproject 
   1. python -m pip instsall django~=3.2
   2. django-admin startproject DDaiso .
   3. python manage.py runserver
   4. Enable Django Support
   5. git 설정
2. startapp product
   1. python manage.py startapp product
   2. 'product', in INSTALLED_APPS in settings
3. product/
   1. models
      1. Product
         1. name
         2. price
         3. python manage.py makemigrations product
            - models -> DB를 만들기 위한 py 만들기
         4. python manage.py migrate product
            - DB를 만들기 위한 py -> DB 테이블 만들기