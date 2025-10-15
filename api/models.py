from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_no=models.IntegerField()
    password=models.CharField(max_length=100)
