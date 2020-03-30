from django.db import models
import pytz
from datetime import datetime

class Member(models.Model):
    okay = models.BooleanField(default = True)

class Profile(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    real_name = models.CharField(max_length=30)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,default='UTC')
    member = models.ForeignKey(Member,related_name = 'members', on_delete=models.CASCADE)


class Activity(models.Model):
    start_time = models.CharField(max_length=50,default = (datetime.now()).strftime("%b %d %Y %H:%M:%S"))
    end_time = models.CharField(max_length=50,default = (datetime.now()).strftime("%b %d %Y %H:%M:%S"),)
    profile = models.ForeignKey(Profile,related_name = 'activity_periods', on_delete=models.CASCADE)
