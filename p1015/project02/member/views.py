from django.shortcuts import render

# Create your views here.
# 로그인
def login(request):
    return render(request, 'login.html')

# 회원가입
def step01(request):
    return render(request, 'step01.html')

def step02(request):
    return render(request, 'step02.html')

def step03(request):
    return render(request, 'step03.html')

def step04(request):
    return render(request, 'step04.html')