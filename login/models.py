from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Event(models.Model):
    school= models.CharField(max_length = 200, default="작성하지 않음")
    event= models.CharField(max_length = 200, default="작성하지 않음")
    event_id= models.IntegerField(default=0)
    place= models.CharField(max_length = 200, default="작성하지 않음")
    time_start= models.TimeField(default = timezone.now)
    time_end= models.TimeField(default = timezone.now)
    description = models.TextField()
    CODE_CHOICES = (
    ("A", "Activity"),
    ("C", "Concert"),
    ("선택하지 않음", "----"),
    )
    code = models.CharField(
    max_length = 200,
    default = "선택하지 않음",
    choices = CODE_CHOICES
    )
    date= models.IntegerField(default=0)

# Create your models here.
# Create your models here.
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    content = models.TextField()

    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    
    allday = models.BooleanField()
    

    def __str__(self):
        return self.title

class Tip(models.Model):    
    body=models.TextField()

    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        blank=True,
                                        related_name='like_user_set',
                                        through='Like')
    @property
    def like_count(self):
        return self.like_user_set.count()

    def summary(self):
        return self.body[:20]

class Review(models.Model):
    body=models.TextField()

    def summary(self):
        return self.body[:20]

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="유저")
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, verbose_name="팁")