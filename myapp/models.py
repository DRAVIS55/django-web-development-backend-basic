from django.db import models

# Create your models here.
class Feature(models.Model):
    tid=models.IntegerField()
    text=models.CharField(max_length=1000)

class Item(models.Model):
    tid = models.IntegerField()
    text = models.CharField(max_length=1000)
