from django.urls import path,include
from . import views

app_name='screen'
urlpatterns = [
    # 영화차트 그래프
    path('s_chart/', views.chart, name='s_chart'),
    # 영화차트 그래프 -ajax
    path('chart_data/', views.chart_data, name='chart_data'),
    # 맵
    path('map/', views.map, name='map'),
    
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