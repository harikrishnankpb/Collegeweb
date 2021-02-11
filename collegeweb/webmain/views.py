from django.shortcuts import render
from django.http import HttpResponse
from webmain.models import Teacher, Student, extendedUser, Subject,Video,Syllabus,Gallary
# Create your views here.
def home(request):
    # return HttpResponse("OM GAM GANESAYA NAMAHA")
    gallary=Gallary.objects.all
    syllabus=Syllabus.objects.all
    return render(request,'index.html',{'gallary':gallary,'syllabus':syllabus})



def studenthome(request):
    student=Student.objects.filter(user=request.user)
    name=student[0].name
    return render(request,"studenthome.html",{'name':name})

def teacherhome(request):
    teacher=Teacher.objects.filter(user=request.user)
    name=teacher[0].name
    # return HttpResponse(teacher[0].name)
    return render(request,"teacherhome.html",{'name':name})

def gallary(request):
    gallary=Gallary.objects.all
    return render(request,'index.html',{'gallary':gallary})

def syllabus(request):
    syllabus=Syllabus.objects.all
    return render(request,'index.html',{'syllabus':syllabus})