from datetime import time

from django.db import models


# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Image = models.ImageField()

    def __str__(self):
        return self.Name


