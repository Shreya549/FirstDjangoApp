from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to  = 'pics')
    