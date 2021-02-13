from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from webmain.models import Teacher, Student, extendedUser, Subject, Video, Referance,Internal,Attendance
from django.http import HttpResponse
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            teacher = Teacher.objects.filter(user=request.user)
            if user.is_superuser == False:
                newuser = extendedUser.objects.filter(user=request.user)
                if newuser[0].isTeacher == True:
                    # teacher session
                    teacher = Teacher.objects.filter(user=user)
                    # return render(request,'index.html',{'teach':1})
                    return redirect('/teacherhome')
                else:
                    # Student session
                    student = Student.objects.filter(user=user)
                    # return render(request,'index.html')
                    return redirect('/studenthome')
            else:
                return redirect("/")
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
        module=request.POST['module']
        sub=Subject.objects.filter(id=subject)
        subname=sub[0].name
        videos = Video(name=videoname, date=dates, ylink=ylink,
                       description='', subject_id=subject,subject_name=subname,module=module)
        videos.save()
        messages.info(request, "Video Saved")
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


def viewvideos(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        videos = Video.objects.filter(subject=subject)
        try:
            return render(request, 'viewvideos.html', {'videos': videos})
        except:
            return HttpResponse(videos)
    if request.user.is_authenticated == True:
        if Student.objects.filter(user=request.user).exists():
            student = Student.objects.filter(user=request.user)
            sem = student[0].sem
            sub = Subject.objects.filter(sem=sem)
            # return HttpResponse(sub)
            return render(request, 'viewvideos.html', {'subjects': sub, 'shows': 1})

        else:
            return redirect("/")
    else:
        return redirect("login")

# Referance

def addreferance(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        dates = request.POST['date']
        flink = request.POST['filelink']
        name = request.POST['fname']
        modulename = request.POST['module']
        description = request.POST['description']
        sub=Subject.objects.filter(id=subject)
        subname=sub[0].name
        reference = Referance(date=dates, flink=flink,name=name,module=modulename,
                              description=description, subject_id=subject,subject_name=subname)
        reference.save()
        messages.info(request, "File saved")
        return redirect(addvideos)
    else:
        if request.user.is_authenticated == True:
            # current_user=request.user
            if Teacher.objects.filter(user=request.user).exists():
                teacher = Teacher.objects.filter(user=request.user)
                sub = Subject.objects.filter(Teacher_name_id=teacher[0])
                # return HttpResponse(sub[0].name)
                return render(request, 'addreferance.html', {'subjects': sub})
            else:
                return HttpResponse("not a teacher")
            # return HttpResponse(current_user.id)
        return redirect('login')


def viewreferance(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        referance = Referance.objects.filter(subject=subject)
        try:
            return render(request, 'viewreferance.html', {'referances': referance})
        except:
            return HttpResponse("Error in referance")
    if request.user.is_authenticated == True:
        if Student.objects.filter(user=request.user).exists():
            student = Student.objects.filter(user=request.user)
            sem = student[0].sem
            sub = Subject.objects.filter(sem=sem)
            return render(request, 'viewreferance.html', {'subjects': sub, 'shows': 1})

        else:
            return redirect("viewreferance")
    else:
        return redirect("login")


def addattendance(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        dates=request.POST['date']
        name=request.POST['filename']
        flink=request.POST['flink']
        sub=Subject.objects.filter(id=subject)
        subname=sub[0].name
        attendance = Attendance(name=name, date=dates, flink=flink, subject_id=subject,subject_name=subname)
        attendance.save()
        messages.info(request, "File saved")
        return redirect("addattendance")
    else:
        if request.user.is_authenticated == True:
            # current_user=request.user
            if Teacher.objects.filter(user=request.user).exists():
                teacher = Teacher.objects.filter(user=request.user)
                sub = Subject.objects.filter(Teacher_name_id=teacher[0])
                # return HttpResponse(sub[0].name)
                return render(request, 'addattendance.html', {'subjects': sub})
            else:
                return HttpResponse("You are not a teacher")
            # return HttpResponse(current_user.id)
        return redirect('login')

def viewattendance(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        attendance = Attendance.objects.filter(subject=subject)
        try:
            return render(request, 'viewattendance.html', {'attendance': attendance})
        except:
            return HttpResponse("Error viewing Attendance")
    if request.user.is_authenticated == True:
        if Student.objects.filter(user=request.user).exists():
            student = Student.objects.filter(user=request.user)
            sem = student[0].sem
            sub = Subject.objects.filter(sem=sem)
            # return HttpResponse(sub)
            return render(request, 'viewattendance.html', {'subjects': sub, 'shows': 1})

        else:
            return redirect("viewattendace")
    else:
        return redirect("login")







# Internal
def addinternal(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        dates=request.POST['date']
        name=request.POST['filename']
        flink=request.POST['flink']
        sub=Subject.objects.filter(id=subject)
        subname=sub[0].name
        internals = Internal(name=name, date=dates, flink=flink, subject_id=subject,subject_name=subname)
        internals.save()
        messages.info(request, "File saved")
        return redirect("addinternal")
    else:
        if request.user.is_authenticated == True:
            # current_user=request.user
            if Teacher.objects.filter(user=request.user).exists():
                teacher = Teacher.objects.filter(user=request.user)
                sub = Subject.objects.filter(Teacher_name_id=teacher[0])
                # return HttpResponse(sub[0].name)
                return render(request, 'addinternal.html', {'subjects': sub})
            else:
                return HttpResponse("You are not a teacher")
            # return HttpResponse(current_user.id)
        return redirect('login')



def viewinternal(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        internal = Internal.objects.filter(subject=subject)
        try:
            return render(request, 'viewinternal.html', {'internal': internal})
        except:
            return HttpResponse("Error viewing Internal")
    if request.user.is_authenticated == True:
        if Student.objects.filter(user=request.user).exists():
            student = Student.objects.filter(user=request.user)
            sem = student[0].sem
            sub = Subject.objects.filter(sem=sem)
            # return HttpResponse(sub)
            return render(request, 'viewinternal.html', {'subjects': sub, 'shows': 1})

        else:
            return redirect("viewinternal")
    else:
        return redirect("login")