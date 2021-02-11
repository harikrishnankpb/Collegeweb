from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
# Create your models here.


class extendedUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    isTeacher=models.BooleanField(default=False)
    isStudent=models.BooleanField(default=False)

class Teacher(models.Model):
    def __str__(self): 
        return self.name
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,default="")
    phnumber=models.CharField(max_length=10)
    qualification=models.CharField(max_length=1000)


class Student(models.Model):
    def __str__(self): 
        return self.name
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,default="")
    sem=models.IntegerField()
    dob=models.DateField()
    phnumber=models.CharField(max_length=10)




class Subject(models.Model):
    def __str__(self): 
        return self.name
    Teacher_name=models.ForeignKey(Teacher,on_delete=models.CASCADE)  # Heare we use tid as teacher_name
    sem = models.IntegerField()  
    name=models.CharField(max_length=100)
    

class Video(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.CharField(max_length=2000)
    ylink = models.CharField(max_length=2000)
    subject_name=models.CharField(max_length=2000)
    module=models.CharField(max_length=100)

class Referance(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200)
    date=models.DateField()
    description=models.CharField(max_length=2000)
    flink=models.CharField(max_length=4000)
    module=models.CharField(max_length=100)
    subject_name=models.CharField(max_length=2000)



class Attendance(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200)
    date=models.DateField()
    flink=models.CharField(max_length=4000)
    subject_name=models.CharField(max_length=1000)
    

class Internal(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200)
    date=models.DateField()
    flink=models.CharField(max_length=4000)
    subject_name=models.CharField(max_length=1000)


class Syllabus(models.Model):
    name=models.CharField(max_length=1000)
    flink=models.CharField(max_length=20000)
    year=models.CharField(max_length=2000)
    date=models.DateField(default=datetime.today())

class Gallary(models.Model):
    name=models.CharField(max_length=1000)
    flink=models.CharField(max_length=20000)
