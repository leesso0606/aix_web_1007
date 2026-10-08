from django.urls import path,include
from . import views

app_name='stuscore'
urlpatterns = [

    path('stu_write/', views.stu_write,name='stu_write'),
]