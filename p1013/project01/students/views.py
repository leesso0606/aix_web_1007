from django.shortcuts import render,redirect
from students.models import Students

# Create your views here.
#  정보 상세보기
# 학생 정보 삭제
def sdelete(request, no):
    Students.objects.get(no=no).delete()
    return redirect('students:slist')





# 학생정보수정 페이지, 저장
def supdate(request, no):
    if request.method=="GET":
        qs=Students.objects.get(no=no)
        context={'stu':qs}
        return render(request, 'supdate.html', context)
    elif request.method=="POST":
        # 수정부분
        qs=Students.objects.get(no=no)
        # 수정 된 데이터
        name= request.POST.get('name')
        major= request.POST.get('major')
        grade= request.POST.get('grade')
        age= request.POST.get('age')
        gender= request.POST.get('gender')
        hobby= request.POST.getlist('hobby')
        #수정된 데이터 반영 
        qs.name=name
        qs.major=major
        qs.grade=grade
        qs.age=age
        qs.gender=gender
        qs.hobby=hobby
        qs.save()
        return redirect('students:slist') #app_name,name방식






# 학생 정보 상세보기 -1개
def sview(request,no):
    qs=Students.objects.get(no=no)
    context={'stu':qs}
    return render(request, 'sview.html',context)




# 학생 정보리스트
def slist(request):
    # 딕셔너리 형태로 데이터를 전달함.
    qs=Students.objects.all().order_by('-no') #데이터 전체 가져오기, 정렬(-역순정렬)
    # qs=Students.objects.get(name='홍길동') #홍길동 데이터 가져오기:1개
    # __contains:포함,__endswith:끝나는 것
    # qs=Students.objects.filter(name__contains='s') #s가 포함된 데이터 가져오기
    # qs=Students.objects.filter(name__endswith='s') #s로 끝나는 데이터
    # gt,gte,lt,lte
    # qs=Students.objects.filter(grade__gte=3='s') #3학년 이상

    context={"list":qs}
    return render(request, 'slist.html',context)



# 학생정보입력 페이지-form전달
def swrite(request):
    if request.method=="GET":
        return render(request, 'swrite.html')
    elif request.method=="POST": #폼으로 값 전달 
        name= request.POST.get('name')
        major= request.POST.get('major')
        grade= request.POST.get('grade')
        age= request.POST.get('age')
        gender= request.POST.get('gender')
        hobby= request.POST.getlist('hobby') #cheakbox는 값이 여러개여서 list로 받아야함

        # save저장
        Students(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby).save()
        # creat저장
        # Students.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby)
        print(name,major,grade,age,gender,hobby)
        return redirect('/')



# html->디장고 데이터 정달 방법
# form, url path, 파라미터, 자바스크립트(ajax)->비동기식



# # 학생정보입력-파라미터 
# def swrite3(request):
#     name= request.GET.get('name')
#     age= request.GET.get('age')
#     print(f'파라미터 값전달:{name},{age}')
#     return redirect('/')



# # 학생정보입력-url path :매개변수로 값 전달
# def swrite2(requset, name):
#     print(f'url path 값전달:{name}')
#     return redirect('/')


