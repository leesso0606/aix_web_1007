from django.db import models
from member.models import Member

# Create your models here.
class Board(models.Model):
    bno =models.AutoField(primary_key=True)
    # 다른 테이블에 primary_key 등록이 되어 있는 것을 다른 테이블에서 사용할 때
    # Borad데이터가 등록될때 Member에서 id값을 확인해서 있는지 체크
    # id =models.CharField(max_length=30) # member-> primary_key
    # Member에 id가 같을 때
    # member= models.ForeignKey(Member, on_delete=models.DO_NOTHING,null=True, blank=True) # id였던걸 다 교체해야함
    # member= models.ForeignKey(Member, on_delete=models.CASCADE,null=True, blank=True) 
    member= models.ForeignKey(Member, on_delete=models.SET_NULL,null=True, blank=True) 
    btitle=models.CharField(max_length=1000)
    bcontent=models.TextField() #대용량 Text
    # 답변달기
    bgroup=models.IntegerField(default=0)
    bstep=models.IntegerField(default=0)
    bindent=models.IntegerField(default=0)    
    bhit=models.IntegerField(default=1)
    bdate=models.DateTimeField(auto_now=True, blank=True)
    bfile=models.ImageField(blank=True,upload_to='board') #upload폴더에 board폴더 생성후 저장

    def __str__(self):
        return f'{self.bno},{self.btitle},{self.bdate}'


    # bno,id,btitle,bcontent,bgroup,bstep,bindent,bhit,bdate,bfile
    # bno: 게시판 번호
    # id: 회원아이디
    # btitle:제목, bcontent:내용
    # bgroup :답변달기 그룹핑 ,bstep:그룹핑순서,bindent:들여쓰기 ->답변달기
    # bhit : 조회수
    # bdate : 등록일
    # bfile : 파일첨부