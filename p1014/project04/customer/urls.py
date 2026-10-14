from django.urls import path,include
from . import views

app_name='customer'

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('notice_view/', views.notice_view, name='notice_view'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('guide/', views.guide, name='guide'),
    path('faq/', views.faq, name='faq'),
]
