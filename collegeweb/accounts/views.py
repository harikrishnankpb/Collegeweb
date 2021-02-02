from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from webmain.models import Teacher, Student, extendedUser, Subject,Video
from django.http import HttpResponse
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # teacher=Teacher.objects.filter(user=request.user)
            if user.is_superuser == False:
                newuser = extendedUser.objects.filter(user=request.user)
                if newuser[0].isTeacher == True:
                    # teacher session
                    teacher = Teacher.objects.filter(user=user)
                    # return HttpResponse(teacher[0].name)
                    return redirect('/')
                else:
                    # Student session
                    student = Student.objects.filter(user=user)
                    # return HttpResponse(student[0].name)
                    return redirect("/")
            else:
                return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# Teacher registraion part


def tregister(requests):
    if requests.method == 'POST':

        name = requests.POST['name']
        password1 = requests.POST['password1']
        email = requests.POST['email']
        username = requests.POST['username']
        password2 = requests.POST['password2']
        phnumber = requests.POST['phnumber']
        qualification = requests.POST['qualification']

        # Verification part

        if password1 != password2:
            messages.info(requests, "Password error")
            return redirect('tregister')
        elif User.objects.filter(username=username).exists():
            messages.info(requests, "Username already exists")
            return redirect('tregister')
        elif User.objects.filter(email=email).exists():
            messages.info(requests, "Email already exists")
            return redirect('tregister')
        try:
            user = User.objects.create_user(
                username=username, password=password1, first_name=name, last_name='Teacher', email=email)
            newTeacher = Teacher(name=name, phnumber=phnumber,
                                 qualification=qualification, user=user)
            user.save()
            newTeacher.save()
            newExtendedUser = extendedUser(
                user=user, isTeacher=True, isStudent=False)
            newExtendedUser.save()
            auth.logout(requests)
            messages.info(requests, 'User registered')
        except:
            messages.info(requests, 'Unexpected error')
    return render(requests, 'tregister.html')


def sregister(requests):
    if requests.method == 'POST':

        name = requests.POST['name']
        sem = requests.POST['sem']
        phnumber = requests.POST['phnumber']
        password1 = requests.POST['password1']
        email = requests.POST['email']
        username = requests.POST['username']
        password2 = requests.POST['password2']
        dob = requests.POST['dob']
        # Verification part

        if password1 != password2:
            messages.info(requests, "Password error")
            return redirect('sregister')
        elif User.objects.filter(username=username).exists():
            messages.info(requests, "Username already exists")
            return redirect('sregister')
        elif User.objects.filter(email=email).exists():
            messages.info(requests, "Email already exists")
            return redirect('sregister')
        try:
            user = User.objects.create_user(
                username=username, password=password1, first_name=name, last_name='', email=email)
            user.save()
            newExtendedUser = extendedUser(
                user=user, isTeacher=False, isStudent=True)
            newExtendedUser.save()
            newStudent = Student(name=name, sem=sem,
                                 phnumber=phnumber, dob=dob, user=user)
            newStudent.save()
            auth.logout(requests)
            messages.info(requests, 'User registered')
        except:
            messages.info(requests, 'Unexpected error')
    return render(requests, 'sregister.html')


def addvideos(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        dates = request.POST['date']
        videoname = request.POST['videoname']
        ylink = request.POST['ylink']
        videos=Video(name=videoname,date=dates,ylink=ylink,description='',subject_id=subject)
        videos.save()
        messages.info(request,"Video Saved")
        return redirect(addvideos)
    else:
        if request.user.is_authenticated == True:
            # current_user=request.user
            if Teacher.objects.filter(user=request.user).exists():
                teacher = Teacher.objects.filter(user=request.user)
                sub = Subject.objects.filter(Teacher_name_id=teacher[0])
                # return HttpResponse(sub[0].name)
                return render(request, 'addvideos.html', {'subjects': sub})
            else:
                return HttpResponse("not a teacher")
            # return HttpResponse(current_user.id)
        return redirect('login')
