from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    passwd = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'