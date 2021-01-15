from django.urls import path
from . import views
urlpatterns=[
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('tregister',views.tregister,name='tregister'),
path('sregister',views.sregister,name='sregister'),
path("addvideos",views.addvideos,name='addvideos')
# path('tregister',views.tregister,name='tregister'),
# path('sregister',views.tregister,name='sregister'),
]
