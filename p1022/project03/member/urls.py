from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('step01/', views.step01, name='step01'),
    path('step02/', views.step02, name='step02'),
    # 이메일전송
    path('email/', views.email, name='email'),
    # 인증키 확인
    path('ekey/', views.ekey, name='ekey'),
]
