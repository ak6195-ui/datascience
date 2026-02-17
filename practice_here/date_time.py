import datetime
# d=datetime.date(2026,2,18)
# print(d)
# dd=datetime.date.today()
# print(dd.day)
# print(dd.weekday()) #MONDAY 0 SUNDAY 6 
# print(dd.isoweekday())# MONDAY 1 SUNDAY 7 
# timedelta= datetime.timedelta(days=3)
# print(dd - timedelta)
# date_bd=datetime.date(2025,9,17)
# timebd= dd - date_bd
# print(timebd.total_seconds())



t=datetime.time(9,30,45,1000)
print(t.hour)
tt=datetime.datetime(2016,7,18,12,30,10,18181)
print(tt)
print(tt.year)
time_delta=datetime.timedelta(hours=7)
print(tt+time_delta)


day_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()
print(day_today)
print(dt_now)
print(dt_utcnow)



import pytz
dt=datetime.datetime(2025,2,17,18,9,45,1999,tzinfo=pytz.UTC)
print(dt)
dtnow=datetime.datetime.now(tz=pytz.UTC)
print(dtnow)
dtn=dtnow.astimezone(pytz.timezone('US/Mountain'))
print(dtn)
for tz in pytz.all_timezones:
    print(tz)
dtus=dtnow.astimezone(pytz.timezone('WET'))
print(dtus)