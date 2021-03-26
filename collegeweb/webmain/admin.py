from django.contrib import admin
from .models import Teacher,Student,extendedUser,Subject,Referance,Video,Gallary,Syllabus,Attendance,Internal

# # Register your models here.
# class VideoAdmin(admin.ModelAdmin):
#     list_display=('name','date','description','ylink')

# class TeacherAdmin(admin.ModelAdmin):
#     list_display=('tid','phnumber','qualification')


class TeacherAdmin(admin.ModelAdmin):
    list_display=('user','name','phnumber','qualification')

class StudentAdmin(admin.ModelAdmin):
    list_display=('user','name','sem','dob','phnumber')

class extendedUserAdmin(admin.ModelAdmin):
    list_display=('user','isTeacher','isStudent')

class subjectAdmin(admin.ModelAdmin):
    list_display=('Teacher_name','sem','name')

class ReferanceAdmin(admin.ModelAdmin):
    list_display=('subject_id','module','name','date','description','flink')

class VideoAdmin(admin.ModelAdmin):
    list_display=('subject_id','module','name','date','description','ylink')

class GallaryAdmin(admin.ModelAdmin):
    list_display=('name','flink')

class SyllabusAdmin(admin.ModelAdmin):
    list_display=('name','flink')

class AttendanceAdmin(admin.ModelAdmin):
    list_display=('subject_name','name','date','flink')

class InternalAdmin(admin.ModelAdmin):
    list_display=('subject_name','name','date','flink')


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Subject,subjectAdmin)
admin.site.register(Referance,ReferanceAdmin)
admin.site.register(Syllabus,SyllabusAdmin)
admin.site.register(Gallary,GallaryAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Internal,InternalAdmin)

