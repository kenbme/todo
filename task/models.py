from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50, default='tasks')
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
