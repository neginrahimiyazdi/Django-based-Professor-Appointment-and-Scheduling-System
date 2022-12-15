import datetime
from testdb.models import Time,User,MH,Meeting,MH_Time
####################################
#functions for mh_get_time_table API

def show_mh_day_meetings(mh_id, date): #select * from meeting where mh_id={} and date={}
    queryset_1 = Time.objects.filter(date=datetime.date(date)).values('time_id')
    queryset_2 = Meeting.objects.filter(MH_id= mh_id, time_id=queryset_1)
    return queryset_2
    #zahra side

#####################################
#functions for get_mh_list API

def show_all_mh_by_name():
    queryset = MH.objects.all().values('first_name','last_name')
    return queryset
    #zahra side

#####################################
#functions for reseve_meeting API

def mh_availabe_time(mh_id, date):  # return all mh  free time
    queryset_1 = Time.objects.filter(date=datetime.date(date)).values('time_id')
    queryset_2 = MH_Time.objects.filter(MH_id= mh_id, time_id= queryset_1)
    return queryset_2
    # zahra side


def remove_mh_available_time(mh_id, date, start_time, end_time):
    queryset_1 = Time.objects.filter(date=datetime.date(date), start_time= datetime.time(start_time), end_time= datetime.time(end_time)).values('time_id')
    queryset_2 = MH_Time.objects.filter(MH_id= mh_id, time_id= queryset_1)
    return queryset_2
    # zahra side


def append_meeting(mh_id, date, start_time, end_time, user_id, subject, description): #reserve meeting
    queryset_1 = Time.objects.filter(date=datetime.date(date), start_time=datetime.time(start_time), end_time=datetime.time(end_time)).values('time_id')
    m = Meeting(subject= subject, description= description, MH_id= mh_id, user_id= user_id, time_id= queryset_1)
    m.save()
    pass  # zahra side
