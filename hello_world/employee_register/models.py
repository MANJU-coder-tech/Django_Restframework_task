from django.db import models


#


class Employee(models.Model):
    user_name = models.CharField(max_length= 20)
    #gender = models.
    email_id = models.EmailField()
    phone_no= models.IntegerField(max_length=13)
    address= models.TextField(max_length= 200)

    objects = models.Manager()






