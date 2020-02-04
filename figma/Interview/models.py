from django.db import models

# Create your models here.
class about(models.Model):
    image_url = models.CharField(max_length = 2083)
    Description = models.CharField(max_length = 255)

class career(models.Model):
    Username = models.CharField(max_length = 2083)
    email = models.CharField(max_length = 255) 
    pdf = models.FileField()