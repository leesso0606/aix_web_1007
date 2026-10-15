from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        rememberId=request.POST.get('rememberId')
        # id와 pw 조건이 맞는 데이터를 여러 개 조회-> 그중 첫번째 데이터를 가져오고 없으면 None로 반환/ get를 쓸경우 데이터가 없으면 에러남.
        qs=Member.objects.filter(id=id,pw=pw).first() 
        if qs:
            request.session['se_id']=id
            request.session['se_nickname']=qs.nickname
            context={'temp':1}
        else:
            context={'temp':0}
        print(f'데이터 확인: {id},{pw}/ 로그인 확인:{context}')
        return render(request,'login.html')