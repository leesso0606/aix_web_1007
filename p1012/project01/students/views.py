from django.shortcuts import render,redirect
from students.models import Students

# Create your views here.
# urls.py 에서 함수로 연결하는 것
# render(): 데이터를 보여 줄 때 / redirect(): 데이터를 저장한 후 다른 페이지로 이동할 때는
# context: render()에 전달할 데이터를 정리해 놓은 변수

# 학생정보 입력 페이지, 저장
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
        
        return redirect('/students/slist/')

# 학생 정보 리스트 :파이썬에서 html로 이동
# /students/slist/에 접속하면 views.slist()가 실행되고, 학생 데이터를 가져와 slist.html에 전달
def slist(request):
    # db에서 전체 리스트 가져오기
    qs=Students.objects.all() #전체 가져오기
    # qs=Students.objects.get(name='홍길동') #1개 만 가져옴
    # qs=Students.objects.filter(name__contains='홍') # 검색해서 여러개 가져옴
    
    context={'list':qs} #딕셔너리 형태 :조회한 데이터를 list라는 이름으로 전달
    return render(request, 'slist.html',context)

# 학생 상세보기
def sview(request,name): # /students/sview/홍길동/ , 특정 정보만 가져오기 때문에 변수에 name가 추가
    print(f'name데이터:{name}')
    qs=Students.objects.get(name=name) #1개의 정보전송
    context={'stu':qs} #조회한 학생을 stu라는 이름으로 HTML에 전달
    return render(request,'sview.html',context)

# 학생정보수정
def supdate(request,name):
    # 기존 정보 보여주기
    if request.method == 'GET':
        print(f'name 수정 페이지 : {name}')
        qs = Students.objects.get(name=name) #1개의 정보전송
        context = {'stu':qs}
        return render(request, 'supdate.html',context)
    # 기존 정보 수정하기
    elif request.method == 'POST':
        print(f'name 수정 완료 : {name}')
        qs = Students.objects.get(name=name) #이전 정보 검색
        if qs:
            name=request.POST.get('name') # html에서 수정한 값 가져오기
            major=request.POST.get('major')
            age=request.POST.get('age')
            grade=request.POST.get('grade')
            gender=request.POST.get('gender')

            qs.name=name # 수정 값 적용하고 저장
            qs.major=major
            qs.age=age
            qs.grade=grade
            qs.gender=gender
            qs.save()
        return redirect('/students/slist/')

# 정보 삭제
def sdelete(request,name):
    Students.objects.get(name=name).delete()
    return redirect('/students/slist/')

# html에서 파이썬 데이터 전달방법
# 1. form
# 2. url 패스 -1개 데이터 전송
# 3. 파라미터
# 4. 자바스크립트