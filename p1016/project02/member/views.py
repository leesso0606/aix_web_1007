from django.shortcuts import render
from member.models import Member

# Create your views here.

#로그아웃
def logout(request):
    request.session.clear()
    context={'temp':2}
    return render(request, 'login.html',context)



# 로그인 정보
def login(request):
    if request.method=='GET':
        cook_id= request.COOKIES.get('cook_id','')
        if cook_id:
            context={'cook_id':cook_id}
        else:
            context={}
        return render(request, 'login.html',context)
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        rememberId=request.POST.get('rememberId') #체크박스여부
        qs=Member.objects.filter(id=id,pw=pw).first()
        if qs: #로그인이 되면
            context={'temp':1}
            request.session['session_id']=id
            request.session['session_nickname']=qs.nickname
        else:
            context={'temp':0}
        print(f'{id},{pw},{rememberId}',context)
        response= render(request, 'login.html',context)
        if rememberId:
            response.set_cookie('cook_id',id,max_age=60*60*24*365)
        else:
            response.delete_cookie('cook_id')
        return response

        
