from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    # image = models.ImageField(upload_to="", default="")
    slug = models.SlugField(unique=True)
