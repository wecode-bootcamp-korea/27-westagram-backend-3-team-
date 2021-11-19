from django.db import models

class Member(models.Model):
    name          = models.CharField(max_length=50)
    email         = models.CharField(max_length=100, unique=True)
    password      = models.CharField(max_length=200)
    phone_number  = models.CharField(max_length=20)
    information   = models.CharField(max_length=200, blank=True, null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'members'
    
    def __str__(self):
        return self.name
