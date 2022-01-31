from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser

admin.site.site_header="ระบบฐานข้อมูลกลาง"
# Register your models here.
class UserModel(UserAdmin):
  pass

admin.site.register(CustomUser, UserModel)  
# Register your models here.

@admin.register(Bkk1001, Bkk1002, Bkk1003, Skw1001, Skw1002, Skw1003)

class ViewAdmin(ImportExportModelAdmin):
	pass
