from django.db import models

class Snip_db(models.Model):
    name =models.CharField(max_length=20)
    ticket_no = models.IntegerField()
    source = models.TextField(max_length=20)
    destination = models.TextField(max_length=20)
    price = models.IntegerField()
    objects = models.Manager()



# Create your models here.
