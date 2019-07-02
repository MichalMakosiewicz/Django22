from django.db import models

# Create your models here.

class blog_post(models.Model):
    title = models.TextField()
    context = models.TextField(null=True, blank=True)
