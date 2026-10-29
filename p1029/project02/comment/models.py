from django.db import models
from event.models import Event
from member.models import Member

# Create your models here.
class Comment(models.Model):
    cno=models.AutoField(primary_key=True)
    event=models.ForeignKey(Event,on_delete=models.CASCADE) # 부모삭제시 모두 삭제 -> 이벤트삭제시 댓글도 삭제
    member=models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True, null=True) #멤버가 탈퇴시 댓글삭제, 빈공간, null 허용
    cpw=models.CharField(max_length=10, blank=True, null=True)
    ccontent=models.TextField(blank=True)
    cdate=models.DateTimeField(auto_now=True)
    # cdate2=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cno},{self.ccontent},{self.cdate}'