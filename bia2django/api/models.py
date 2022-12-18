from django.db import models
from django.db import migrations
import datetime


# Create your models here.
class Time(models.Model):
    date =  models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return "%s %s" % (self.date, self.start_time)

class MH(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    mh_email = models.EmailField(max_length=100)
    mh_password = models.CharField(max_length=100)
    teacher_number = models.CharField(max_length=50)
    degree = models.CharField(max_length= 100)
    field = models.CharField(max_length= 100)
    link_to_webpage = models.CharField(max_length= 1000)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class User(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    student_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length= 50)
    degree = models.CharField(max_length= 100)
    field = models.CharField(max_length= 100)
    university = models.CharField(max_length= 100)
    adviserID = models.ForeignKey(MH, on_delete=models.CASCADE)
    #guider_id = models.ForeignKey(MH, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Meeting(models.Model):
    subject = models.CharField(max_length= 100,default=None)
    rate = models.IntegerField(default=None)
    description = models.TextField(default=None)
    was_holded = models.BooleanField(default=None)
    mhID = models.ForeignKey(MH, on_delete=models.CASCADE)
    userID  = models.ForeignKey(User, on_delete=models.CASCADE)
    timeID  = models.ForeignKey(Time, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.meeting_id)

class MH_Time(models.Model) :
    mhID = models.ForeignKey(MH, on_delete=models.CASCADE)
    timeID = models.ForeignKey(Time, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.id)