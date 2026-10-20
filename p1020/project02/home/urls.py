from django.urls import path,include
from . import views

app_name=''
urlpatterns = [
    path('', views.index, name='index'),
]

# '': 접속할 주소 -> member의 'login/' 처럼
# views.index : 실행할 함수
# name='index' : url에 붙인 이름 
#  따라서 사용자가 / 에 접속하면 views.py 의 index() 함수가 실행된다.