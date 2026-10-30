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
from event.models import Event
from member.models import Member
from comment.models import Comment

# Create your views here.
# 04. 댓글수정저장
def commUpdate(request):
    cno=request.POST.get('cno')
    ccontent=request.POST.get('ccontent')
    # 1.수정
    Comment.objects.filter(cno=cno).update(ccontent=ccontent) # .update() → 기존 데이터를 직접 수정하고, 수정 대상이 된 행 개수를 반환
    qs=Comment.objects.filter(cno=cno).values()
    l_qs=list(qs)
    context={'result':'성공','comment':l_qs}

    # 2.수정
    # qs = Comment.objects.get(cno=cno)
    # qs.ccontent = ccontent
    # qs.save()

    return JsonResponse(context)



# 03. 댓글삭제
def commDelete(request):
    cno=request.POST.get('cno')
    Comment.objects.get(cno=cno).delete()
    context={'result':'성공'}
    return JsonResponse(context)



# 02.댓글리스트
def commlist(request):
    context={'result':'성공'}
    return JsonResponse(context)

# 01.댓글등록 - ajax
def commWrite(request):
    # 현재 보고 있는 게시글의 번호를 AJAX이 Django에게 전달
    eno=request.POST.get('eno')
    # DB에서 해당 번호의 게시글 객체 1개를 가져옴 : ForeignKey는 객체1개 전체를 입력해야 함.
    e_qs = Event.objects.get(eno=eno)
    m_qs = Member.objects.get(id=request.session['session_id'])
    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent')

    # Comment저장 - qs:cno,event,member,cpw,ccontent,cdate
    qs = Comment.objects.create(
        event=e_qs,member=m_qs,cpw=cpw,ccontent=ccontent)
    print(f'확인:{eno},{cpw},{ccontent},{qs.cno},{qs.cdate}')
    
    # Json타입으로 변경
    qs_1 = list(Comment.objects.filter(cno=qs.cno).values())
    context = {'result':'성공','comment':qs_1}
    return JsonResponse(context)