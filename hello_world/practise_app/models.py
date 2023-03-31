from django.db import models

class MYTEST(models.Model):
    na=models.CharField(max_length=10)
    num=models.IntegerField()
    pwd=models.TextField(max_length=12)
    objects=models.Manager()

# Create your models here.
