# creating user
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # currently broken image upload:
    # image = models.ImageField(upload='static/images/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True, 
        null=True
    )
