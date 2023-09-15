from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class vlog(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank= True)

class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    userid=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self): 
        return self.userid


class Checkout(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    address2=models.CharField(max_length=122)
    country=models.CharField(max_length=122)
    state=models.CharField(max_length=122)
    zipp=models.TextField(max_length=8)
    card_name=models.TextField(max_length=21)
    card_no=models.TextField(max_length=12)
    card_ex=models.TextField(max_length=3)
    card_cvv=models.TextField(max_length=4)
    date=models.DateField()

    def __str__(self): 
        return self.fname