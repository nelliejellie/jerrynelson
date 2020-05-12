from django.db import models
from datetime import datetime

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=300)
    link = models.CharField(max_length=100, null=True)

class Services(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=300)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    subject = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=300)
    email = models.EmailField()


