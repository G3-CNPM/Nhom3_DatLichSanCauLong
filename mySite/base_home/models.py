from django.db import models

# Create your models here.

class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)
    
    def __str__(self):
        return self.fname + ' ' + self.lname

class Vatdung(models.Model):
    vname = models.CharField(max_length=100)
    vorigin = models.CharField(max_length=100)
    vmdate = models.DateField(auto_now_add=False)
    vprice = models.IntegerField()

    def __str__(vatdung):
        return vatdung.vname
    
class Doannuoc(models.Model):
    fname = models.CharField(max_length=100)
    forigin = models.CharField(max_length=50)
    fmdate = models.DateField()
    fexp = models.DateField()
    fprice = models.IntegerField()
    
    def __str__(fnd):
        return fnd.fname
        
class Payment(models.Model):
    pname = models.CharField(max_length=100)
    pacc = models.CharField(max_length=50)
    pmethod = models.CharField(max_length=50)
    pamount = models.IntegerField()
    pdes = models.TextField()
    
    def __str__(pay):
        return pay.pname + ' ' + pay.pmethod

class Booking(models.Model):
    bname = models.CharField(max_length=100)
    btime = models.TimeField()
    bprice = models.IntegerField()
    
    def __str__(booking):
        return booking.bname
    
    