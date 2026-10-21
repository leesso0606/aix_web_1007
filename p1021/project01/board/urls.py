from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('chart/', views.chart, name='chart'),
    path('chart_data/', views.chart_data, name='chart_data'),
    
    path('bwrite/', views.bwrite, name='bwrite'),
    path('blist/', views.blist, name='blist'),
    path('bview/<int:bno>/', views.bview, name='bview'),
    path('bupdate/<int:bno>/', views.bupdate, name='bupdate'),
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'),
]



# 보내는 방법 :html->디장고
# 1. form -> 회원가입, 게시판
# 2. url path -> 게시판 bno
# 3. 파라미터 -> 하단 넘버링 page/?page=1
# 4. 자바스크립트(ajax, axis)->차트

# 받는 방법
# 1. context
# 2. 자바스크립트 (ajax,axis)
# 3. 파라미터(거의 사용 안함)-> redirect('/')