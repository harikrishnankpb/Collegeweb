from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class MyAppUser( models.Model ) :
#     def __unicode__( self ) :
#        return self.user.username
#     user    = models.ForeignKey( User ,on_delete=models.CASCADE)
#     comment = models.TextField( blank = True )
#     isTeacher   = models.BooleanField( )

class Teacher(models.Model):
    def __str__(self): 
        return "something"
    # tid = models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    tid=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phnumber=models.CharField(max_length=12)
    qualification=models.CharField(max_length=1000)

class Subject(models.Model):
    # subid = models.IntegerField()
    sem = models.IntegerField()
    name=models.CharField(max_length=100)
    tid=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    

class Video(models.Model):
    # vid = models.IntegerField()
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.CharField(max_length=2000)
    ylink = models.CharField(max_length=2000)



# class Attendance(models.Model):
#     Attendance = models.DateField()


# class Assignment(models.Model):
#     aid = models.IntegerField()
#     flink = models.CharField(max_length=2000)



# class Student(models.Model):
#     sid = models.IntegerField()
#     sem = models.IntegerField()
#     dob = models.DateField()
#     phnumber = models.IntegerField()
