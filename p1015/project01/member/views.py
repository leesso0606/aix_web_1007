from django.shortcuts import render
from member.models import Member

# Create your views here.

# logout
def logout(request):
    request.session.clear() #섹션 모두 삭제
    # del request.session['session.nickname'] # 섹션 1개만 삭제
    context={'temp':2}
    return render(request, 'login.html',context)


# 로그인: GET,POST
def login(request):
    if request.method=='GET':
        context={}
        if request.COOKIES.get('cookie_id'): #없을때 None
            context={'cookie_id':request.COOKIES.get('cookie_id')} 
        return render(request, 'login.html',context)
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        idsave=request.POST.get('idsave','') #idsave 값이 있을 때 가벼오고 없을 때는 빈공백처리
        # 회원확인 2
        qs=Member.objects.filter(id=id,pw=pw).first() #qs,None
        if qs:
            # 섹션 추가
            request.session['session_id']=qs.id
            request.session['session_nickname']=qs.nickname
            context={'temp':1}
        else:
            context={'temp':0}

        print(f'로그인 정보:{id},{pw},{idsave}/ 회원확인:{context}')
        # return render(request, 'login.html',context) #context는 파이썬에서 html로 보내는 방법
        response= render(request, 'login.html',context) #쿠키사용을 위해
        if idsave !='': #쿠키저장
            response.set_cookie('cookie_id',id,max_age=60*60*24*365) #60초*60분*24시간*365일
        else: #쿠키삭제
            response.delete_cookie('cookie_id') 
        return response
    
        # 회원확인1
        # try:
        #     qs=Member.objects.get(id=id,pw=pw) #db에 회원이 존재하는지 체크
        #     # 섹션
        #     request.session['session_id']=qs.id
        #     request.session['session_nickname']=qs.nickname
        #     context={'temp':1}
        # except Member.DoesNotExist:
        #     context={'temp':0}
            
        # python ->html : context
        # html->python : form,url path, 파라미터, 자바스크립트(ajax)

def step01(request):
    return render(request, 'step01.html')

def step02(request):
    return render(request, 'step02.html')

def step03(request):
    return render(request, 'step03.html')

def step04(request):
    return render(request, 'step04.html')