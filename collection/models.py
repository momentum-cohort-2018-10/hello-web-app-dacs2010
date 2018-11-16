from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # picture = models.ImageField(upload='thing_images/')
    slug = models.SlugField(unique=True)
