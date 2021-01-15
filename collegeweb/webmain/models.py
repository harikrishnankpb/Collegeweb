from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class MyAppUser( models.Model ) :
#     def __unicode__( self ) :
#        return self.user.username
#     user    = models.ForeignKey( User ,on_delete=models.CASCADE)
#     comment = models.TextField( blank = True )
#     isTeacher   = models.BooleanField( )
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
    # isTeachear=models.BooleanField(default=False)


class Student(models.Model):
    def __str__(self): 
        return self.name
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,default="")
    # age=models.IntegerField()
    sem=models.IntegerField()
    dob=models.DateField()
    phnumber=models.CharField(max_length=10)




class Subject(models.Model):
    # subid = models.IntegerField()
    def __str__(self): 
        return self.name
    Teacher_name=models.ForeignKey(Teacher,on_delete=models.CASCADE)  # Heare we use tid as teacher_name
    sem = models.IntegerField()  
    name=models.CharField(max_length=100)
    

class Video(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    # sem=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.CharField(max_length=2000)
    ylink = models.CharField(max_length=2000)







# class Attendance(models.Model):
#     Attendance = models.DateField()


# class Assignment(models.Model):
#     aid = models.IntegerField()
#     flink = models.CharField(max_length=2000)


