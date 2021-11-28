from django.db                  import models
from django.db.models.deletion  import CASCADE
from core.models                import TimeStampModel



class Post(TimeStampModel):
    user       = models.ForeignKey('users.User', on_delete = models.CASCADE)
    image      = models.URLField(max_length = 200)  #charfield??? 유효화 검사가 안되는 거면 charfield사용 하면 상관 없음???사상누각 콘상누각
    describe   = models.CharField(max_length = 2000, null=True)
    #created_at = models.DateTimeField(auto_now_add = True)
    #updated_at = models.DateField(auto_now = True)
    
    class Meta:
        db_table = 'postings'

