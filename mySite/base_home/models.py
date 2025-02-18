from django.db import models

# Create your models here.

class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)
    birth = models.DateField()
    telephn = models.IntegerField()
    
    def __str__(self):
        return self.fname + ' ' + self.lname

class Vatdung(models.Model):
    vname = models.CharField(max_length=100)
    