
from django.db import models

# Create your models here.


class list1(models.Model):
    name=models.CharField(max_length=255)
    image=models.CharField(max_length=2555)

