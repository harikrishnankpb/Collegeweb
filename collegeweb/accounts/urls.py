from django.urls import path
from . import views
urlpatterns=[
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('tregister',views.tregister,name='tregister'),
path('sregister',views.sregister,name='sregister'),
path("addvideos",views.addvideos,name='addvideos'),
path("viewvideos",views.viewvideos,name='viewvideos'),
path("viewreferance",views.viewreferance,name='viewreferance'),
path("addreferance",views.addreferance,name='addreferance'),
path("viewattendance",views.viewattendance,name='viewattendance'),
path("addattendance",views.addattendance,name='addattendance'),
path("viewinternal",views.viewinternal,name='viewinternal'),
path("addinternal",views.addinternal,name='addinternal'),
]
