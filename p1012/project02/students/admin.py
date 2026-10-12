from django.contrib import admin #Django에서 제공하는 관리자 페이지 기능을 가져와
from students.models import Students #students 앱의 models.py 파일에서 Students 클래스를 가져와.
                                        #Students는 데이터베이스 테이블과 연결되는 모델

# Register your models here.
admin.site.register(Students) 
#admin :Django의 관리자 기능 , site: 관리자 사이트, register(): 등록하다, Students:등록할 모델 클래스