from django.shortcuts import render

# Create your views here.
# 학생성적 입력 페이지
def swrite(request):
    return render(request, 'swrite.html')
# 학생성적 출력 페이지
def slist(request):
    return render(request, 'slist.html')


# request는 사용자가 브라우저에서 서버로 보낸 요청 정보를 담고 있는 객체