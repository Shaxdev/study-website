from django.contrib import admin
from  . import models
# Register your models here.

class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['ism', 'familya', 'sharif']
    search_fields = ['ism', 'familya', 'sharif']

admin.site.register(models.UserInfo, ProfileInfoAdmin)


class ECodesAdmin(admin.ModelAdmin):
    list_display = ['user', 'code']
    search_fields = ['code']
    
admin.site.register(models.EmailCode, ECodesAdmin)