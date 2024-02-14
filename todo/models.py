from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Todo(models.Model):
    text = models.CharField(max_length = 255)
