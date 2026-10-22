from django.shortcuts import render
import os
from pathlib import Path
from dotenv import load_dotenv
from django.db.models import F,Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib                             
from email.mime.text import MIMEText
import random
import string
import json

# Create your views here.

#  인증키 확인-서버에서 확인할 것(보안상)


def ekey(request):
    ekey=request.POST.get('ekey','')
    print(f'인증키 확인:{ekey}')
    s_ekey=request.session['session_e_key']
    if ekey==s_ekey:
        context={'temp':1} #인증성공
    else:
        context={'temp':0} #인증실패
    return JsonResponse(context)




# 이메일 전송
def email(request):
    # 1. 이메일 주소
    email=request.POST.get('email','')
    print(f'데이터 확인:{email}')           #cmd창에서 보임 -> 없다면 url.py, ajax의 url등 확인
    # context={'email':'email'}             #console창에서 보임.
    # return JsonResponse(context)            # 두 가지가 정상이라면 AJAX와 Django의 연결은 성공


    # 2. 네이버 비밀번호 가져오기(.env)
    BASE_DIR =Path(__file__).resolve().parent.parent
    ENV_FILE =BASE_DIR /'.env'
    load_dotenv(ENV_FILE)
    naver_key=os.getenv('naver_key')
    print('환경변수 로드:', bool(naver_key))    # True가 출력되면 환경변수에 값이 존재

    # 3. 인증키 생성
    #       0-9문자열 + a-z까지 문자열 
    chars = string.digits + string.ascii_lowercase
    # 중복가능:choices, 중복불가:sample / 리스트 -> 문자열
    e_key = ''.join(random.choices(chars,k=10)) 
    print('e_key',e_key)

    # 4. 이메일내용 - 글자로 이메일발송
    sendEmail = 'leesso0606@naver.com' # 보내는사람
    content = f'이메일확인 인증키 : {e_key}'

    # 5. 정보그룹핑
    msg = MIMEText(content)
    msg['From'] = sendEmail # 보내는사람
    msg['To'] = email                # 받는사람
    msg['Subject'] = '이메일 TEST2'    # 제목

    # 6. 그룹핑 정보전송
    s = smtplib.SMTP("smtp.naver.com",587) #SMTP 서버
    s.starttls() # 메일서버접근
    s.login(sendEmail,naver_key) # 메일서버로그인
    s.sendmail(sendEmail,email,msg.as_string()) # 메일발송
    s.close() # 메일닫기

    request.session['session_e_key'] = e_key #python manage.py migrate를 해야만 진행가능
    context = {'e_key':e_key}

    return JsonResponse(context)







def step01(request):
    # 디펙토리 위치 :부모의 부모로 가서
    BASE_DIR =Path(__file__).resolve().parent.parent
    ENV_FILE =BASE_DIR /'.env'
    load_dotenv(ENV_FILE)
    naver_key=os.getenv('naver_key')
    return render(request, 'step01.html')


def step02(request):
    return render(request, 'step02.html')