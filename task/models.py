from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date = models.DateField()
    ends_in = models.CharField(max_length=5)  # 17:23 H:M
