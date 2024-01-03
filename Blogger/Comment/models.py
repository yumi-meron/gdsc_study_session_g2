from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

# Create your models here.
