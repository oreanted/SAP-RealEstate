import email
from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    description = models.TextField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.name
        
