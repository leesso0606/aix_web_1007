from django.urls import path,include
from.import views

app_name='board'
urlpatterns = [
    path('bwrite/', views.bwrite, name='bwrite'),
    path('blist/',views.blist, name='blist.html'),
    path('bview/<int:bno>/',views.bview, name='blist.bview'),
    path('bupdate/<int:bno>/',views.bupdate, name='blist.bupdate'),
    path('bdelete/<int:bno>/',views.bdelete, name='blist.bdelete'),
    
]