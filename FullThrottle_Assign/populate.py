import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FullThrottle_Assign.settings')

import django
django.setup()

from user_app.models import Profile,Member,Activity
from datetime import datetime

m = Member(okay=True)
m.save()
p = Profile(real_name = 'Egon Spengler',timezone='America/Los_Angeles',member = m)
p.save()
a = Activity(start_time =(datetime(2016, 3, 7, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2018, 5, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p )
a.save()
a1 = Activity(start_time =(datetime(2018, 3, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2019, 5, 6, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p )
a1.save()
a2 = Activity(start_time =(datetime(2019, 8, 12, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2020, 3, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p )
a2.save()

p1 = Profile(real_name = 'Glinda Southgood',timezone='Asia/Kolkata',member = m)
p1.save()
a3 = Activity(start_time =(datetime(2016, 3, 7, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2018, 5, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p1 )
a3.save()
a4= Activity(start_time =(datetime(2018, 3, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2019, 5, 6, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p1 )
a4.save()
a5 = Activity(start_time =(datetime(2019, 8, 12, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2020, 3, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p1 )
a5.save()

p2= Profile(real_name = 'John',timezone='Asia/Kolkata',member = m)
p2.save()
a6 = Activity(start_time =(datetime(2016, 3, 7, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),end_time=(datetime(2018, 5, 29, 21, 41, 58, 13589).strftime("%b %d %Y %H:%M:%S")),profile= p2 )
a6.save()
