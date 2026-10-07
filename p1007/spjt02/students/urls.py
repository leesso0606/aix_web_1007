
from django.urls import path,include
# from django.urls import include 하거나 위에 include 를 붙이거나
from . import views #자기 폴더 안 views를 가져와라

urlpatterns = [
    path('s_write/', views.s_write), #students app안에 url를 찾아감
]