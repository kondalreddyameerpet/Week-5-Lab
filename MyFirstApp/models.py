from django.db import models
from django.db.models.base import Model

# Create your models here.
class FirstAppExample(models.Model):
    data = models.JSONField()