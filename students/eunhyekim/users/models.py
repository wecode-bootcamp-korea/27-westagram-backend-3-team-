from django.db                      import models
from core.models                    import TimeStampModel

class User(TimeStampModel):
    name       = models.CharField(max_length = 45)
    email      = models.CharField(max_length = 200, unique = True)
    password   = models.CharField(max_length = 200)
    contact    = models.CharField(max_length = 200)
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateField(auto_now = True)
    
    class Meta:
        db_table = 'users'