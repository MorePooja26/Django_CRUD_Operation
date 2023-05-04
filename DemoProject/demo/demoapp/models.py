from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    contact=models.IntegerField()
    address=models.CharField(max_length=255)
