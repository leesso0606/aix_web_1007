from django.shortcuts import render,redirect
from member.models import Member #여기에 데이터가 있음, 연결

# Create your views here.

# 회원 수정 페이지 
def mupdate(request,id):
    if request.method=='GET':
        print(f'확인데이터:{id}')
        qs=Member.objects.get(id=id)
        tel=qs.tel.split('-') #010-0000-0000->[010,0000,0000] 로 분리된다
        context={'member':qs, 'tel':tel}
        return render(request, 'mupdate.html',context, )
    elif request.method=='POST':
        # id=request.session.session_id
        pw=request.POST.get('pw')
        name=request.POST.get('name')
        nickname=request.POST.get('nickname')
        tel1=request.POST.get('tel1')
        tel2=request.POST.get('tel2')
        tel3=request.POST.get('tel3')
        tel=f'{tel1}-{tel2}-{tel3}'
        gender=request.POST.get('gender')
        hobby=request.POST.get('hobby')
        # id로 검색
        qs=Member.objects.get(id=id)
        qs.pw=pw
        qs.name=name
        qs.nickname=nickname
        qs.tel=tel
        qs.gender=gender
        qs.hobby=hobby
        qs.save()

        # db에 저장
        # Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel, gender=gender, hobby=hobby).save()
    
        print(f'{id},{pw},{name},{nickname},{tel},{gender},{hobby}')
        return redirect ('/')


# =======================================================================
#  회원가입 페이지 : get,post
def mwrite(request):
    if request.method=='GET':
        return render(request, 'mwrite.html')
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        name=request.POST.get('name')
        nickname=request.POST.get('nickname')
        tel1=request.POST.get('tel1')
        tel2=request.POST.get('tel2')
        tel3=request.POST.get('tel3')
        tel=f'{tel1}-{tel2}-{tel3}'
        gender=request.POST.get('gender')
        hobby=request.POST.get('hobby')

        # db에 저장
        # Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel, gerder=gender, hobby=hobby).save()
        Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel, gender=gender, hobby=hobby)

        print(f'{id},{pw},{name},{nickname},{tel},{gender},{hobby}')
        return render(request, 'mresult.html')

# ==========================================================================
# 로그아웃
def logout(request):
    context={'temp':2}
    request.session.clear()
    return render(request, 'login.html', context)



# ==================================================================================
# 로그인 페이지:get, 로그인 확인:post
def login(request):
    # 맨 처음 로그인 화면 들어갈 때
    if request.method=='GET':
        cook_id= request.COOKIES.get('cook_id','') #없으면 공백
        if cook_id:
            context ={'cook_id':cook_id}
        else:
            context={}
        return render(request, 'login.html', context)
    # form에 정보를 출력할 때 
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        rememberId=request.POST.get('rememberId') #체크박스 안되어 있으면 None, 되어 있으면 on

        #db 확인
        qs=Member.objects.filter(id=id,pw=pw).first()
        if qs: # 로그인 성공
            context={'temp':1}
            # 섹션추가
            request.session['session_id']=id
            request.session['session_nickname']=qs.nickname
        else: #로그인 실패
            context={'temp':0}

        print(f'데이터 확인:{id},{pw},{rememberId}/ {context}')
        # 쿠키 적용
        response=render(request, 'login.html', context)
        if rememberId:
            response.set_cookie('cook_id',id,max_age=60*60*24*365)
        else:
            response.delete_cookie('cook_id')
        return response
