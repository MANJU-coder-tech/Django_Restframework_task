from django.db import models
from django.core.validators import RegexValidator
class Signin(models.Model):
    user_name = models.CharField(max_length= 20)
    email_id = models.EmailField()
    phone_no= models.IntegerField(max_length=13)
    address= models.TextField(max_length= 200)

    password2 = models.CharField(max_length=20)
    password_validator=RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@#$%^&*+=-])[a-zA-Z\\d@#$%^&*-=+]{8,}$',)
    password=models.CharField(max_length=20, validators=[password_validator])
    objects = models.Manager()