from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.
def logout(request):
    request.session.clear() #섹션모두삭제
    context = {'temp':2} 
    return render(request, 'login.html', context)

def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        print(f'로그인정보 : {id},{pw}')
        try:
            qs=Member.objects.get(id=id,pw=pw)
            request.session['session_id']=qs.id
            request.session['session_nickname']=qs.nickname
            context={'temp':1}
            return render(request, 'login.html', context)
        except Member.DoesNotExist:
            context={'temp':0}
            return render(request, 'login.html', context)