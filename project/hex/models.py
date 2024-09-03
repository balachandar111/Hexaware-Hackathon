from django.db import models

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=20,default="")
    Address=models.CharField(max_length=20,default="")
    Password=models.CharField(max_length=20,default="")
    Cpassword=models.CharField(max_length=20,default="")
    
    
   
    
