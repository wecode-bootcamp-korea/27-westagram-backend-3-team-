from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=20)
    person_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'members'
    
    def __str__(self):
        return self.name
