from django.contrib import admin
from face_as.models import student, Lastface

class studentAdmin(admin.ModelAdmin):
    list_display=('id','name','roll_number','gender','email','phone','branch','sem','subject','image')

class LastFaceAdmin(admin.ModelAdmin):
    list_display=('last_face','date')

admin.site.register(student,studentAdmin)
admin.site.register(Lastface,LastFaceAdmin)
# Register your models here.
