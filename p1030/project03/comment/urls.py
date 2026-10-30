from django.urls import path,include
from . import views

app_name='comment'
urlpatterns = [
    path('event/', views.event, name='event'),
    path('eview/', views.eview, name='eview'),
]