from django.shortcuts import render,redirect
from students.models import Students

# Create your views here.
def swrite(request):
    if request.method=='GET':
        return render(request, 'swrite.html')
    elif request.method=='POST':
        name=request.POST.get('name') #데이터가 없어도 에러가 나지 않음.
        major=request.POST.get('major') 
        grade=request.POST.get('grade') 
        age=request.POST.get('age') 
        gender=request.POST.get('gender') 
        # 1. save()로 저장하는 방법
        qs=Students(name=name,major=major,age=age,grade=grade,gender=gender)
        qs.save()
        # 2. create()
        # Students.objects.create(name=name,major=major,age=age,grade=grade,gender=gender)
        print(f'확인:{name},{major}')
        # gender=request.POST.get['gender'] #데이터가 없으면 에러가 남 
        
        return redirect('/students/slist')


def slist(request):
    # db 에서 전체 리스트 가져오기
    qs=Students.objects.all()
    context={'list':qs}
    return render(request, 'slist.html',context)

def sview(request,name):
    print(f'name데이터:{name}')
    qs=Students.objects.get(name=name) #1개의 정보전송
    context={'stu':qs}
    return render(request,'sview.html',context)

# html에서 파이썬 데이터 전달방법
# 1. form
# 2. url 패스 -1개 데이터 전송
# 3. 파라미터
# 4. 자바스크립트