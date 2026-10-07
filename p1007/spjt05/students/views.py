from django.shortcuts import render

# Create your views here.
# 학생성적 입력 페이지
def swrite(request):
    return render(request, 'swrite.html')
# 학생성적 출력 페이지
def slist(request):
    return render(request, 'slist.html')