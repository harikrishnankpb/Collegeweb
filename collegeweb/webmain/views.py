from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("OM GAM GANESAYA NAMAHA")
    return render(request,'index.html')
