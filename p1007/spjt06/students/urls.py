
from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    # url(swrite), views파일에서 swrite함수 찾음
    path('swrite/', views.swrite, name='swrite'),

]