from django.shortcuts import render
from board.models import Board

# Create your views here.



def blist(request):
    qs=Board.objects.all()
    context={'list':qs}
    return render(request,'blist.html',context)




# 글쓰기 페이지 연결 :get, 저장:post
def bwrite(request):
    if request.method=="GET":
        return render(request,'bwrite.html')
    elif request.method=="POST":
        btitle = request.POST.get('btitle')
        # bfile = request.POST.get('bfile')
        bfile = request.FILES.get('bfile')
        Board(btitle=btitle,bfile=bfile).save()
        print(f'데이터 확인:{btitle},{bfile}')
        return render(request,'bwrite.html')
