from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('blist/', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
]
# 파일업로드시 url구성이 되어 있어야 파일을 업로드할수 있음.
# urlpatterns += static(settings.MEDIA_URL,
# document_root = settings.MEDIA_ROOT
# )