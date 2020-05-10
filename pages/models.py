from django.db import models
from datetime import datetime

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=300)

class Services(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=300)