from django.db import models

# Create your models here.
class Member(models.Model):
    # primary_key=True : 중복불가, null불가
    # Feoreignkey 외래키 :다른 클래스에서 primarykey로 사용된 것을 사용할 때 

    id = models.CharField(max_length=30,primary_key=True)
    pw = models.CharField(max_length=100)
    # name,nickname,tel,gender,hobby
    name=models.CharField(max_length=60)
    nickname=models.CharField(max_length=60)
    tel=models.CharField(max_length=20) #000-1111-1111
    gender=models.CharField(max_length=10) #남자, 여자
    hobby=models.CharField(max_length=100)
    mdate=models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.id},{self.pw},{self.nickname},{self.hobby},{self.mdate}'