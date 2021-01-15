from django.contrib import admin
from .models import Teacher,Student,extendedUser,Subject

# # Register your models here.
# class VideoAdmin(admin.ModelAdmin):
#     list_display=('name','date','description','ylink')

# class TeacherAdmin(admin.ModelAdmin):
#     list_display=('tid','phnumber','qualification')


class TeacherAdmin(admin.ModelAdmin):
    list_display=('user','name','phnumber','qualification')


class extendedUserAdmin(admin.ModelAdmin):
    list_display=('user','isTeacher','isStudent')

class subjectAdmin(admin.ModelAdmin):
    list_display=('Teacher_name','sem','name')


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student)
admin.site.register(extendedUser,extendedUserAdmin)
admin.site.register(Subject,subjectAdmin)