from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class KursModel(models.Model):
    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'
    title = models.CharField(max_length=30)
    added_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Qoshilgan vaqti')
    
    def __str__(self):
        return self.title


class MainModel(models.Model):
    class Meta:
        verbose_name = 'Asosiy Model'
        verbose_name_plural = 'Asosiy Modellar'
    kurs_id = models.ForeignKey('KursModel', on_delete=models.CASCADE,  verbose_name='Kurs')
    title = models.CharField(max_length=50)
    position = models.PositiveIntegerField(verbose_name='Positsiyasi', help_text='qayerda kelishini korsating Masalan: 1 yoki 5 orinda kelsin')
    
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Bajarilmoqda', 'Bajarilmoqda'),
        ('Tugatildi', 'Tugatildi'),
        ('Failing', 'Failing'),
    )

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Active')
    
    addet_at = models.DateTimeField(auto_now_add=True, verbose_name='Model qoshilgan vaqt')
    
    def __str__(self):
        return self.title


class InsideModel(models.Model):
    class Meta:
        verbose_name = 'Model uchun malumot(content, video, file...)'
        verbose_name_plural = 'Model uchun malumot(content, video, file...)lar'
    position = models.PositiveIntegerField(null=True)  
    m_id = models.ForeignKey(MainModel, on_delete=models.CASCADE, null=True, verbose_name='Qoshmoqchi bolgan malumotingiz modulini tanlang')
    title = models.CharField(max_length=40, verbose_name='Mavzu')
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    

class InlineModelContent(models.Model):
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
    inside_model = models.ForeignKey(InsideModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    content = RichTextUploadingField(null=True, blank=True)



# class DOCMODELS(models.Model):
#     class Meta:
#         verbose_name = 'Document'
#         verbose_name_plural = 'Documnets'
    
#     inside_model = models.ForeignKey(InsideModel, on_delete=models.CASCADE, null=True) 
#     added_at = models.DateTimeField(auto_now_add=True)
    
# class DocumentContent(models.Model):
#     class Meta:
#         verbose_name = 'Content'
#         verbose_name_plural = 'Content'
#     document_id = models.ForeignKey(DOCMODELS, on_delete=models.CASCADE, null=True, verbose_name='Document')
#     title = models.CharField(max_length=100, null=True)
#     content = RichTextUploadingField(null=True, blank=True)

    
# class DocumentFile(models.Model):
    
#     document_id = models.ForeignKey(DOCMODELS, on_delete=models.CASCADE, null=True, verbose_name='Document')
#     title = models.CharField(max_length=50, null=True)
#     file = models.FileField(upload_to='static/documents/files', blank=True, help_text='Documentlar kiriting')
#     downloadable = models.BooleanField()
    
    

class FileModel(models.Model):
    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
    

    inside_model = models.ForeignKey(InsideModel, on_delete=models.CASCADE, null=True)
    TYPE_CHOICES = (
        ('Prezintatsiya', 'Prezintatsiya'),
        ('Video', 'Video'),
        ('Documents', 'Documents'),
    )
    title = models.CharField(max_length = 50, null=True, blank=True)
    file_type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=True, help_text='File turini tanlang')
    file_link = models.CharField(max_length=400, null=True, blank=True)
    file = models.FileField(upload_to='static/documents/files',blank=True, null=True, help_text='Hatoliklar bolmasligi uchun Tanlagan Tipingizdagi filenigina yuklang')
    downloadable = models.BooleanField()


class DescriptModel(models.Model):
    class Meta:
        verbose_name = 'Kurs uchun description'
        verbose_name_plural = 'Kurs uchun descriptionlar'
        
    m_id = models.ForeignKey(KursModel, on_delete=models.CASCADE, null=True, verbose_name='Kurs')
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'static/Models/images')    
    
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class DesContentModel(models.Model):# Contentlar uchun 
    des = models.ForeignKey(DescriptModel, on_delete=models.CASCADE,  null=True, verbose_name='Description Model')

    title = models.CharField(max_length=25, null=True)
    content = RichTextField(verbose_name = 'Conent', null=True)
    
    
    
