from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.hashers import make_password,check_password

class User(AbstractUser):
    name = models.CharField(max_length=250,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=250,null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True,upload_to='profile/')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Student(models.Model):
    name = models.CharField(max_length=250,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=250,null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True,upload_to='profile/')
    grade = models.CharField(max_length=20, null=True)
    schoolname = models.TextField(null=True)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self,raw_password):
        return check_password(raw_password,self.password)

class Teacher(models.Model):
    name = models.CharField(max_length=250,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=250,null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True,upload_to='profile/')
    graderange = models.CharField(max_length=20, null=True)
    schoolname = models.TextField(null=True)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self,raw_password):
        return check_password(raw_password,self.password)

class EntranceQuestion(models.Model):
    question = models.TextField()
    a=models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()
    answer = models.CharField(max_length=1)
    explain = models.TextField(null=True)
    year = models.IntegerField()
    subject = models.TimeField()
    unit = models.IntegerField()
    
class ClassRoom(models.Model):
    teacher=models.IntegerField()
    name = models.TextField()
    created = models.DateTimeField(auto_now=True)
    
class ClassRoomStudent(models.Model):
    classroom = models.IntegerField()
    student = models.IntegerField()
    


class ClassRoomPost(models.Model):
    classroom = models.IntegerField()
    author = models.IntegerField()
    tasktype = models.TextField()
    title = models.TextField()
    file = models.FileField(null=True,upload_to='file/')
    image = models.ImageField(null=True,upload_to='image/')
    text = models.TextField()

class QuestionComment(models.Model):
    question = models.IntegerField()
    author = models.IntegerField()
    text = models.TextField()
    file = models.FileField(null=True,upload_to='file/')
    image = models.ImageField(null=True,upload_to='image/')