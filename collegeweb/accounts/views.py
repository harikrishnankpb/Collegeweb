from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def tregister(requests):
    if requests.method=='POST':

        name=requests.POST['name']
        subject=requests.POST['subject']
        password1=requests.POST['password1']
        email=requests.POST['email']
        username=requests.POST['username']
        password2=requests.POST['password2']

        # Verification part

        if password1!=password2:
            messages.info(requests,"Password error")
            return redirect('tregister')
        elif User.objects.filter(username=username).exists():
            messages.info(requests,"Username already exists")
            return redirect('tregister')
        elif User.objects.filter(email=email).exists():
            messages.info(requests,"Email already exists")
            return redirect('tregister')

        user=User.objects.create_user(username=username,password=password1,first_name=name,last_name=subject,email=email)
        user.save()

    return render(requests,'tregister.html')


    