from django.shortcuts import render
import os
from pathlib import Path
from dotenv import load_dotenv
from member.models import Member
from django.db.models import F,Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib                             
from email.mime.text import MIMEText
import random
import string

# Create your views here.
# 이메일 전송
def emailsend(request):
    return

# 로그아웃
def logout(request):
    request.session.clear()
    context={'temp':2}
    return render(request,'login.html',context)


# 로그인
def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        qs=Member.objects.filter(id=id,pw=pw).first()
        if qs:
            temp=1
            request.session['session_id']=qs.id
            request.session['session_nickname']=qs.nickname
        else:
            temp=0
        context={'temp':temp}
    return render(request, 'login.html',context)

#  회원가입 1단계
def step01(request):
    return render(request, 'step01.html')