from datetime import datetime
from time import timezone
from django.db import models

# Create your models here.

class Doctors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    role  = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)

class Blog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s %s %s" %(self.sNo, self.title, self.slug)

from django.contrib.auth.models import AbstractUser
class Userinfo(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_doctor = models.BooleanField(null=True)
    is_patient = models.BooleanField(null=True)

    def __str__(self):
        return self.username

class Patients(models.Model):
     firstname = models.CharField(max_length=100)
     lastname = models.CharField(max_length=100)
     treat_dept = models.CharField(max_length=100)
     address = models.CharField(max_length=100)
     phonenum = models.IntegerField(default=0)
     emailid = models.EmailField(unique=True)
     bloodgroup = models.CharField(max_length=100)

     def __str__(self):
         return "%s %s %s %s" %(self.firstname, self.lastname, self.treat_dept,self.phonenum)

    

