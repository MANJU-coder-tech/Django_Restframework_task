from django.db import models


# Create your models here.
class adding(models.Model):
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    #res=models.IntegerField()
    objects = models.Manager()


