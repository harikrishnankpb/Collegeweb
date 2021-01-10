from django.contrib import admin
from .models import Video,Subject,Teacher

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display=('name','date','description','ylink')

class TeacherAdmin(admin.ModelAdmin):
    list_display=('tid','phnumber','qualification')

admin.site.register(Video,VideoAdmin)
admin.site.register(Subject)
admin.site.register(Teacher,TeacherAdmin)
# admin.site.register(MyAppUser)