from django.urls import path,include
from .import views

app_name='' #안 넣으면 에러남. 중요
urlpatterns = [
    path('', views.index, name='index'),
]