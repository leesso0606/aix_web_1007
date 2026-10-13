from django.contrib import admin
from students.models import Students

# Register your models here.
admin.site.register(Students)


# admin.py 에 작성 후 관리자에 db생성하기
# db생성할것이 있는지 확인
# python manage.py makemigrations
# db생성
# python manage.py migrate