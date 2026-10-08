from django.shortcuts import render
from stuscore.models import Stu_write
# Create your views here.
def stu_write(request):
    if request.method=='GET':
        print("GET페이지가 로딩")
        return render(request, 'stu_write.html')
    elif request.method=='POST':
        print("POST페이지가 로딩")
        name=request.POST.get('name')
        no=request.POST.get('no')
        school=request.POST.get('school')
        grade=request.POST.get('grade')
        stature=request.POST.get('stature')
        kor=request.POST.get('kor')
        eng=request.POST.get('eng')
        math=request.POST.get('math')
        sw=request.POST.get('sw')
        print(name,no,school,grade,stature,kor,eng,math,sw)
        qs=Stu_write(name=name,no=no,school=school,grade=grade,stature=stature,kor=kor,eng=eng,\
                    math=math,sw=sw)
        qs.save()
        return render(request,'stu_write.html')