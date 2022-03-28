from tkinter import CASCADE
from django.db import models

# Create your models here.
class admin_reg(models.Model):
    adminid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.EmailField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)


class platform(models.Model):
    platformid=models.AutoField(primary_key=True)
    adminid=models.ForeignKey(admin_reg, on_delete=models.CASCADE)
    platform_name=models.CharField(max_length=20)
    description=models.CharField(max_length=30)
    image=models.FileField(upload_to='images',default='default.jpg')

class project(models.Model):
    projectid=models.AutoField(primary_key=True)
    platformid=models.ForeignKey(platform, on_delete=models.CASCADE)
    project_name=models.CharField(max_length=20)
    documentation=models.CharField(max_length=50)
    project=models.FileField(upload_to='projects')