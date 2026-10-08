from django.shortcuts import render,redirect
from students.models import Stu

# 학생성적입력
def swrite(request):
    # 처음 페이지 들어갈 때 보통 GET로 요청. 그래서 처음 들어갈 때만 
    if request.method == 'GET':
        print("get페이지가 로딩")
        return render(request,'swrite.html')
    elif request.method == 'POST':
        print("post페이지가 로딩")
        name=request.POST.get('name')
        major=request.POST.get('major')
        grade=request.POST.get('grade')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        qs=Stu(name=name,major=major,grade=grade,age=age,gender=gender)
        qs.save()
        print(name,major,grade,age,gender)
        return redirect('/students/slist/')
        # return render(request,'swrite.html') # 변수 싹 주석하고 print와 이것만 주석 풀면 html은 그대로 cmd에서만 print출력
    # elif request.method == 'PUT':
    #     pass
    # elif request.method == 'DELETE':
    #     pass

# 학생성적리스트
def slist(request):
    return render(request,'slist.html')