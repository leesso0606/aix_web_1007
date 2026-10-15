from django.contrib import admin
from member.models import Member
# python manage.py makemigrations ->python manage.py migrate-> 다음 db 만들기
# Register your models here.
admin.site.register(Member)