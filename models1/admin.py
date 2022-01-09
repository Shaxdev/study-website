from django.contrib import admin
from django.db.models import fields

# from apps
from . import models

# Register your models here.
class KursAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'added_at']
    search_fields = ['title']
    
admin.site.register(models.KursModel, KursAdmin)

class MainModelAdmin(admin.ModelAdmin):
    list_display = ['kurs_id', 'title', 'position', 'status', 'addet_at']
    search_fields = ['title', 'status']
    
admin.site.register(models.MainModel, MainModelAdmin)


class InlineModelContentAdmin(admin.StackedInline):
    model = models.InlineModelContent
    fields = ['title', 'content']
    extra = 0


class FileModelAdmin(admin.StackedInline):
  
    model = models.FileModel
    fields = ['file_type', 'file', 'file_link']
    search_fields = ['file_type']
    extra = 0
    
class InsideModelAdmin(admin.ModelAdmin):
    
    list_display = ['m_id', 'title', 'added_at']
    search_fields = ['title']
    
    inlines = [InlineModelContentAdmin, FileModelAdmin]
    
admin.site.register(models.InsideModel, InsideModelAdmin)



class DesContentModelAdmin(admin.StackedInline):
    model = models.DesContentModel
    fields = ['title', 'content']
    extra = 1
    
class DescriptionModelAdmin(admin.ModelAdmin):
    list_display = ['m_id', 'title', 'subtitle', 'added_at']
    search_fields = ['title', 'subtitle']
    
    inlines = [DesContentModelAdmin]
    
admin.site.register(models.DescriptModel, DescriptionModelAdmin)



