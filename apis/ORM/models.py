from django.db import models


# Create your models here.
class Time(models.Model):
    time_id = models.IntegerField()
    date =  models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Meeting(models.Model):
    meeting_id = models.IntegerField()
    MH_id = models.IntegerField()
    user_id = models.IntegerField()
    time_id = models.IntegerField()
    subject = models.CharField(max_length= 500)
    #report = models.CharField()
    rate = models.IntegerField()
    description = models.TextField()
    was_holded = models.BooleanField()

class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    user_email = models.EmailField()
    student_number = models.IntegerField()
    mobile_number = models.CharField(max_length= 15)
    degree = models.CharField(max_length= 100)
    field = models.CharField(max_length= 300)
    university = models.CharField(max_length= 200)
    adviser_id = models.IntegerField()
    guider_id = models.IntegerField()
    #

class MH(models.Model):
    MH_id = models.IntegerField()
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    MH_email = models.EmailField()
    teacher_number = models.IntegerField()
    degree = models.CharField(max_length= 100)
    field = models.CharField(max_length= 300)
    link_to_webpage = models.CharField(max_length= 1000)
    QR = models.

class MH_Time(models.Model) :
    id = models.IntegerField()
    MH_id = models.IntegerField()
    time_id = models.IntegerField()
