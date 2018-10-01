from django.db import models

# Create your models here.
class Wallet(models.Model):
    label = models.CharField(max_length=255)
    address = models.CharField(max_length=255,unique=True)
    balance = models.IntegerField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    

class Group(models.Model):
    title = models.CharField(max_length=255)