from django.db                      import models
from django.db.models.deletion      import CASCADE
from django.db.models.lookups       import IntegerFieldFloatRounding

class User(models.Model):
    name     = models.CharField(max_length = 45)
    email    = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    contact  = models.CharField(max_length = 45)
    
    class Meta:
        db_table = 'users'



