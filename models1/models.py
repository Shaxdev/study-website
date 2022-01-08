from django.db import models
from ckeditor.fields import RichTextField

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
        ('Tugatildi', 'Tugatildi'),
        ('Failing', 'Failing'),
    )

    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Active')
    
    addet_at = models.DateTimeField(auto_now_add=True, verbose_name='Model qoshilgan vaqt')
    
    def __str__(self):
        return self.title


class InsideModel(models.Model):
    class Meta:
        verbose_name = 'Model uchun malumot(content, video, file...)'
        verbose_name_plural = 'Model uchun malumot(content, video, file...)lar'
    
    m_id = models.ForeignKey(MainModel, on_delete=models.CASCADE, null=True, verbose_name='Qoshmoqchi bolgan malumotingiz modelini tanlang')
    title = models.CharField(max_length=40)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class InlineModelContent(models.Model):
    position = models.PositiveIntegerField(null=True)
    inside_model = models.ForeignKey(InsideModel, on_delete=models.CASCADE, null=True)
    content = RichTextField(null=True, blank=True)

class FileModel(models.Model):
    
    inside_model = models.ForeignKey(InsideModel, on_delete=models.CASCADE, null=True)
    position = models.PositiveIntegerField(null=True)
    TYPE_CHOICES = (
        ('Prezintatsiya', 'Prezintatsiya'),
        ('Document', 'Document'),
        ('Video', 'Video'),
    )
    file_type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=True, help_text='File turini tanlang')
    file_link = models.CharField(max_length=400, null=True, blank=True)
    file = models.FileField(upload_to='static/documents/files',blank=True, null=True, help_text='Hatoliklar bolmasligi uchun Tanlagan Tipingizdagi filenigina yuklang')


class DescriptModel(models.Model):
    class Meta:
        verbose_name = 'Model uchun description'
        verbose_name_plural = 'Model uchun descriptionlar'
        
    m_id = models.ForeignKey(MainModel, on_delete=models.CASCADE, null=True, verbose_name='Model')
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
    
    

class TestModel(models.Model):
    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Test'
    m_id = models.ForeignKey(MainModel, on_delete = models.CASCADE, null=True) 
    # md_id = main_model.
    title = models.CharField(max_length=50)
    TIME_CHOICES = (
        (0, 0),
        (10, 10),
        (20, 20),
        (30, 30),
        (40, 40),
        (60, 60),
        (90, 90),
    )
    time_limit = models.IntegerField(choices=TIME_CHOICES, default = 0 ,null=True, help_text='Agar testni vaqtini cheklamoqchi bolsangis quyiydagilardan birini tanlang!')
    added_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Qoshilgan vaqti')
    def __str__(self):
        return f'Model: {self.m_id} \nTest: {self.title}'

    
class QuestionModel(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
    test = models.ForeignKey(TestModel, on_delete=models.CASCADE,   null=True)
    question = RichTextField(null=True)
    
    def __str__(self):
        return self.question

class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE,  null=True, verbose_name='Question')
    answer = RichTextField(null=True)
    is_correct = models.BooleanField(default=False )
