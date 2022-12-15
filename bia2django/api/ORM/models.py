from django.db import models
from django.db import migrations
import datetime


# Create your models here.
class Time(models.Model):
    time_id = models.BigAutoField(primary_key=True)
    date =  models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return "%s %s" % (self.date, self.start_time)

class MH(models.Model):
    MH_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    MH_email = models.EmailField()
    teacher_number = models.IntegerField()
    degree = models.CharField(max_length= 100)
    field = models.CharField(max_length= 300)
    link_to_webpage = models.CharField(max_length= 1000)
    #QR = models.

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    user_email = models.EmailField()
    student_number = models.IntegerField()
    mobile_number = models.CharField(max_length= 15)
    degree = models.CharField(max_length= 100)
    field = models.CharField(max_length= 300)
    university = models.CharField(max_length= 200)
    #adviser_id = models.IntegerField()
    #guider_id = models.IntegerField()
    adviser_id = models.ForeignKey(MH, on_delete=models.CASCADE)
    #guider_id = models.ForeignKey(MH, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Meeting(models.Model):
    meeting_id = models.BigAutoField(primary_key=True)
    #MH_id = models.IntegerField()
    #user_id = models.IntegerField()
    #time_id = models.IntegerField()
    subject = models.CharField(max_length= 500,default=None)
    rate = models.IntegerField(default=None)
    description = models.TextField(default=None)
    was_holded = models.BooleanField(default=None)
    MH_id = models.ForeignKey(MH, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_id = models.ForeignKey(Time, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.meeting_id)

class MH_Time(models.Model) :
    id = models.BigAutoField(primary_key=True)
    #MH_id = models.IntegerField()
    #time_id = models.IntegerField()
    MH_id = models.ForeignKey(MH, on_delete=models.CASCADE)
    time_id = models.ForeignKey(Time, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.id)
################CREATING OBJECTS#################
date_list=[]
for i in range(0,5):
    # time(year = 0, month = 0, day = 0)
    date_list.append(datetime.date(1997, 10, 19))
start_time_list=[]
end_time_list=[]
for i in range(0,5):
    # time(hour = 0, minute = 0, second = 0)
    start_time_list.append(datetime.time(8+i,0,0))
    end_time_list.append(datetime.time(9+i,0,0))

for i in range(0,5) :
    t = Time(date=date_list[i],start_time=start_time_list[i],end_time=end_time_list[i])
    t.save()