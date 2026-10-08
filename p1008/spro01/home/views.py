from django.shortcuts import render
# render:html을 열어줘

# Create your views here.
# 메인페이지 -templates폴더->index.html
def index(request):
    return render(request, 'index.html')
