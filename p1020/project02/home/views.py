from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')



# def : 함수를 만들겠다는 선언
# index: 함수이름
# request는 사용자가 브라우저에서 서버로 보낸 요청 정보를 담고 있는 객체
# return: 함수의 결과를 돌려준다.
# render(): HTML 템플릿으로 응답을 만든다.
# 'index.html': 보여줄 HTML 파일 이름