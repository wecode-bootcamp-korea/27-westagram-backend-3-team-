from django.db import models

# Create your models here.

class User(models.Model):
    name       = models.CharField(max_length=45)
    email      = models.CharField(max_length=200, unique=True)
    passwd     = models.CharField(max_length=200)
    phone      = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'users'
