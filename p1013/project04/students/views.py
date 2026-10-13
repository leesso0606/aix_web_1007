from django.shortcuts import render,redirect
from students.models import Students

# Create your views here.

# 학생 정보 삭제
def sdelete(request,no):
    Students.objects.get(no=no).delete()
    return redirect('students:slist')

# 학생정보수정,저장
def supdate(request,no):
    if request.method=="GET":
        # 데이터 출력-1개
        qs=Students.objects.get(no=no)
        context={'stu':qs}
        return render(request, 'supdate.html',context)
    elif request.method=="POST":
        # 수정할 데이터 -1개
        qs=Students.objects.get(no=no)
        # 수정된 데이터
        name=request.POST.get('name')
        major=request.POST.get('major')
        grade=request.POST.get('grade')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        # 수정 반영
        qs.name=name
        qs.major=major
        qs.grade=grade
        qs.age=age
        qs.gender=gender
        qs.hobby=hobby
        qs.save()
        return redirect('students:slist') #app_name:name

# 학생정보상세보기
def sview(request,no):
    # 특정 데이터 출력
    qs=Students.objects.get(no=no)
    context={'stu':qs}
    return render(request, 'sview.html',context)

# 학생정보리스트
def slist(request):
    # 모든 db정보 출력(역순정렬)
    qs=Students.objects.all().order_by('-no')
    context={'list':qs}
    return render(request,'slist.html',context)



#  학생정보입력
def swrite(request):
    if request.method=="GET":
        return render(request, 'swrite.html')
    elif request.method=="POST":
        name=request.POST.get('name')
        major=request.POST.get('major')
        grade=request.POST.get('grade')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        Students(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby ).save()
        print(name,hobby) #관리자에서 저장되었는지 확인용
        return redirect('/')