from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F,Q
from django.conf import settings
from django.conf.urls.static import static
import os
from member.models import Member
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# 차트그래프
def chart(request):
    # # id_list=['aaa','bbb','ccc','ddd','eee','fff']
    # qs=Board.objects.all().order_by('bno')[:6] #6개만
    # qs_value=list(qs.values())

    # id_list=[1,2,3,4,5,6]
    # bhit_list=[19,20,21,26,40,70]
    # print(qs_value)
    # context={'id_list':id_list,'bhit_list':bhit_list}
    return render (request, 'chart.html')

# 차트데이터
# ajxa페이지 이동
@csrf_exempt
def chart_data(request):
    id_list=['aaa','bbb','ccc','ddd','eee','fff']
    bhit_list=[19,20,21,26,40,70]
    data={'id_list':id_list,'bhit_list':bhit_list }

    # db에서 가져와서 차트그래프 그리기 진행예정
    return JsonResponse(data)



# 게시글 리스트
# 검색 get=페이지 열기 ,post= 검색
def blist(request):
    if request.method=='GET':
        qs=Board.objects.all().order_by('-bgroup','bstep')
        # 페이징 처리----------------------------------------------------

        pg = Paginator(qs,20) #5줄씩 리턴
        page =int(request.GET.get('page',1)) # 정수변환-> 요청한 페이지 번호 가져오기, 없으면 1
        qs =pg.get_page(page) # 해당 페이지의 게시글 가져오기

        # -------------------------------------------------------
        context={'list':qs, 'page':page}
        return render(request,'blist.html',context)
    elif request.method=='POST':
        
        #  검색부분---------------------------------------
        category = request.POST.get('category')
        search_word = request.POST.get('search_word')
        
        # category -btitle
        if category == 'btitle':
            qs=Board.objects.filter(btitle__contains=search_word).order_by('-bgroup','bstep')
        elif category == 'bcontent':
            qs=Board.objects.filter(bcontent__contains=search_word).order_by('-bgroup','bstep')
        else:
            qs=Board.objects.filter\
                (Q(btitle__contains=search_word)|Q(bcontent__contains=search_word))\
                    .order_by('-bgroup','bstep')

        # 검색        
        # qs=Board.objects.filter\
        #     (Q(bno__gte=30)|Q(bhit__lte=50))\
        #     .order_by('-bgroup','bstep')

        # id가 s가 들어가면서 조회수가 50이상인것을 검색하시오
        qs=Board.objects.filter\
            (Q(id__icontains='s')|Q(bhit__gte=50))\
            .order_by('-bgroup','bstep')
        print('개수:', qs.count()) #cmd창에서 나옴


        # 페이징 처리----------------------------------------------------

        pg = Paginator(qs,20) #5줄씩 리턴
        page =int(request.GET.get('page',1)) # 정수변환-> 요청한 페이지 번호 가져오기, 없으면 1
        qs =pg.get_page(page) # 해당 페이지의 게시글 가져오기

        # -------------------------------------------------------
        context={'list':qs, 'page':page} # 파이썬 딕셔너리로 HTML에 전달할 데이터 묶기
        return render(request,'blist.html',context)









# 게시글 상세보기
def bview(request,bno):
    # # board에 1개 검색
    # qs=Board.objects.get(bno=bno)
    # qs.bhit=qs.bhit+1
    # qs.save()

    #  데이터 1개 가져오기
    qs=Board.objects.filter(bno=bno) #.first() # 왼쪽 bno는 DB 필드 이름, 오른쪽 bno는 함수에서 전달받은 변수
    qs.update(bhit=F('bhit')+1) #F: qs에 있는 컬럼값을 가져올 때 사용
    context={'board':qs[0]}
    return render(request,'bview.html',context)







# 게시글 삭제
def bdelete(request,bno):
    Board.objects.get(bno=bno).delete()
    context={'temp':0,'bno':bno}
    return render(request,'bwrite.html',context)


# 게시글 수정
# GET - 수정페이지, POST - 수정저장
def bupdate(request,bno):
    if request.method=='GET':
        qs=Board.objects.get(bno=bno) # 기존게시물을 가지고 페이지 입장.
        context={'board':qs}
        return render(request,'bupdate.html',context)
    
    elif request.method=='POST':
        btitle=request.POST.get('btitle')
        # id=request.POST.get('id')
        bcontent=request.POST.get('bcontent')
        bfile=request.FILES.get('bfile')
        old_file=request.FILES.get('old_file')

        qs=Board.objects.get(bno=bno) # 기존게시물을 가지고 페이지 입장.
        qs.btitle=btitle # 기존 제목과 내용을 변경
        qs.bcontent=bcontent
        if bfile:
            qs.bfile=bfile

        qs.save() # 변경한 내용을 저장.
        context={'temp':2,'bno':bno}
        return render(request,'bwrite.html',context)





# 게시글 등록
# get:페이지 열기, post: html에서 체출된 값을 가져와 저장
def bwrite(request):
    if request.method=='GET':
        return render(request,'bwrite.html')
    elif request.method=='POST':
        btitle=request.POST.get('btitle')
        id=request.POST.get('id')
        bcontent=request.POST.get('bcontent')
        bfile=request.FILES.get('bfile')
        # db에 저장
        # create()
        qs= Board.objects.create(btitle=btitle, id=id, bcontent=bcontent, bfile=bfile)
        # 답변달기를 할 경우
        qs.bgroup=qs.bno
        qs.save()
        # # save()
        # qs= Board(btitle=btitle, id=id, bcontent=bcontent, bfile=bfile).save()
        context={'temp':1}
        print(f'데이터 확인:{btitle},{id},{bcontent},{bfile}')
        return render(request, 'bwrite.html',context)


    