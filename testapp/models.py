from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sliders(models.Model):
    image=models.ImageField(upload_to='sliders/')
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    

class AboutSection(models.Model):
    image1=models.ImageField(upload_to='about/')
    image2=models.ImageField(upload_to='about/')
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)
    description=models.TextField()
    sub_heading=models.CharField(max_length=100)
    my_list = models.JSONField(default=list)

    def __str__(self):
        return self.title
class Services(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    icon=models.ImageField(upload_to='services/icon/')

    def __str__(self):
        return self.title
    
