from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    updated=models.DateTimeField(default=datetime.now(),blank=True)
