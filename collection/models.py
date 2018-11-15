from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(upload_to="", default="static/thing_images/deafault")
    slug = models.SlugField(unique=True)