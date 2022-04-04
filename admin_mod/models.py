from argparse import ONE_OR_MORE
from django.contrib.auth.models import User
from django.db import models


class platform(models.Model):
    platformid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    platform_name=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    image=models.FileField(upload_to='images',default='default.jpg')

class project_table(models.Model):
    projectid=models.AutoField(primary_key=True)
    platformid=models.ForeignKey(platform, on_delete=models.CASCADE)
    project_name=models.CharField(max_length=50)
    documentation=models.CharField(max_length=100)
    project=models.FileField(upload_to='projects')

class mcq(models.Model):
    mcqid=models.AutoField(primary_key=True)
    platformid=models.ForeignKey(platform, on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=30)
    option1=models.CharField(max_length=30)
    option2=models.CharField(max_length=30)
    option3=models.CharField(max_length=30)
    option4=models.CharField(max_length=30)