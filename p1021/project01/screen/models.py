from django.db import models

# Create your models here.
class Screen(models.Model):
    sno=models.AutoField(primary_key=True)
    rank=models.IntegerField(default=0)
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True, blank=True)
    percent=models.FloatField(default=0)
    revenue=models.IntegerField(default=0)
    crevenue=models.IntegerField(default=0)
    sales=models.IntegerField(default=0)
    csales=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.sno},{self.rank},{self.title}'


# 21억을 넘으면 BigIntegerField()
# FloatField : 소수점
# IntegerField : 정수