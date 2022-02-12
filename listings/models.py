from django.db import models
from realtors.models import Realtor
# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    description  = models.TextField(max_length=255)
    price = models.IntegerField()
    badrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title