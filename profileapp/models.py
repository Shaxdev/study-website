from django.db import models

# Create your models here.

class ProfileModel(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    ism = models.CharField(max_length=30)
    familya = models.CharField(max_length=35)
    sahrif = models.CharField(max_length=35)
    
    image = models.ImageField(max_size = 2Mb)