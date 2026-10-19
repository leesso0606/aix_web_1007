from django.shortcuts import render
from board.models import Board

# Create your views here.
# 게시글 삭제
def bdelete(request,bno):
    Board.objects.get(bno=bno).delete()
    context={'temp':0,'bno':bno}
    return render(request, 'bwrite.html',context)


# 게시판 수정하기
def bupdate(request,bno):
    if request.method=='GET':
        qs=Board.objects.get(bno=bno)
        context={'board':qs}
        return render(request, 'bupdate.html',context)
    elif request.method=='POST':
        btitle = request.POST.get('btitle')
        id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        qs=Board.objects.get(bno=bno)
        qs.btitle=btitle
        qs.bcontent=bcontent
        if bfile:
            qs.bfile=bfile
        qs.save()

        context={'temp':2, 'bno':bno}
        return render(request, 'bwrite.html',context)


# 게시판 리스트
def blist(request):
    qs=Board.objects.all().order_by('-bgroup','bstep')
    context={'list':qs}
    return render(request, 'blist.html',context)

# 게시판 글쓰기
def bwrite(request):
    if request.method=='GET':
        return render(request, 'bwrite.html')
    elif request.method=='POST':
        btitle = request.POST.get('btitle')
        id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        qs=Board.objects.create(btitle=btitle,id=id,bcontent=bcontent,bfile=bfile)
        qs.save()
        context={'temp':1}
        print(f'데이터확인 : {btitle},{id},{bcontent},{bfile},')
        return render(request, 'bwrite.html',context)


# 게시글 상세보기
def bview(request, bno):
    qs=Board.objects.filter(bno=bno).first()
    qs.bhit+=1
    context={'board':qs}
    return render(request, 'bview.html',context)