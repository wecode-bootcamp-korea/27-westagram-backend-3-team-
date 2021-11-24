from django.db                  import models
from django.db.models.deletion  import CASCADE


class Post(models.Model):
    user       = models.ForeignKey('users.User', on_delete = models.CASCADE)
    image      = models.URLField(max_length = 200)
    describe   = models.CharField(max_length = 2000, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    #updated_at = models.DateField(auto_now = True)
    
    class Meta:
        db_table = 'postings'

