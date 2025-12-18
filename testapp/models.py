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