from django.db import models
from account.models import User
from .validators import validate_file_size
# Create your models here.
# from django.contrib.auth.models import User 

    
class UserInfo(models.Model):
    class Meta:
        verbose_name = 'Users information'
        verbose_name_plural = 'Users informations'
        
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ism = models.CharField(max_length=30, null=True)
    familya = models.CharField(max_length=35, null=True)
    sharif = models.CharField(max_length=35, null=True)
    image = models.ImageField(upload_to = 'static/images/profile_img', validators=[validate_file_size])

    def __str__(self):
        return f'{self.user}'
    
    
    
def generate_email_code():
    import random
    import string
    available_characters = string.ascii_letters + string.digits
    code = ''
    for i in range(8):
        index = random.randint(0, len(available_characters)-1)
        code += available_characters[index]  
    return code
    
    

class EmailCode(models.Model):
    class Meta:
        verbose_name = "Code which is sended to user's email"
        verbose_name_plural = "Codes which is sended to users's emails"
        
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    code = models.CharField(max_length=8, default=generate_email_code())
    is_active = models.BooleanField(default=True)
    
    sended_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        
        return f'email: {self.user.email} \nCode: {self.code}'
    
    
# class UserInfo1(models.Model):
#     class Meta:
#         verbose_name = 'Users information'
#         verbose_name_plural = 'Users informations'
        
#     user = models.ForeignKey('User', models.CASCADE, null=True)
#     ism = models.CharField(max_length=30, null=True)
#     familya = models.CharField(max_length=35, null=True)
#     sharif = models.CharField(max_length=35, null=True)
#     image = models.ImageField(upload_to = 'static/images/profile_img', validators=[validate_file_size])
