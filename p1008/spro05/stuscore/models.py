from django.db import models

# Create your models here.
# 학생 정보를 저장할 테이블을 만든다
# CharField는 문자열(텍스트)
# max_length=100 → 최대 100글자까지 저장
# IntegerField는 정수를 저장
# default=0 :값을 입력하지 않았을 때 기본값으로 0을 넣는다
# FloatField는 실수를 저장
class Stu_write(models.Model):
    name = models.CharField(max_length=100)
    no = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    stature = models.FloatField(default=0)
    kor = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    sw = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name},{self.no},{self.school},{self.grade},{self.stature},{self.kor},{self.eng},{self.math},{self.sw}'