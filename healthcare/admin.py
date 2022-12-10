from django.contrib import admin
# from .models import Doctors, Role, Department
from .models import Doctors,Blog,Userinfo,Patients
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display=["id","first_name","dept","phone"]
class BlogAdmin(admin.ModelAdmin):
    list_display=["sNo","title","slug"]
class UserinfoAdmin(admin.ModelAdmin):
    list_display=["username"]
class PatientAdmin(admin.ModelAdmin):
    list_display=["firstname","lastname","treat_dept","phonenum"]



admin.site.register(Doctors,DoctorAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Userinfo,UserinfoAdmin)
admin.site.register(Patients,PatientAdmin)



