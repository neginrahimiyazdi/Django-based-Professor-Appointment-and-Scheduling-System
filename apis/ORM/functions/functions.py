#functions for mh_fill_timetable API

import datetime
from testdb.models import Time,User,MH,Meeting,MH_Time
#?
def remove_mh_day_meetings(mh_id, date):  # remove * from meetings where mh_id={} and date={}
    queryset = Time.objects.filter(date=datetime.date(date)).values('time_id')
    try :
        records = Meeting.objects.get(mh_id = mh_id , time_id= queryset)
        records.delete()
        print("Records deleted successfully!")
    except :
        print("Records doesn't exist")
    pass  # zahra side


def append_time(date, start_time, end_time):  # append a time and return its id
    # time(year = 0, month = 0, day = 0)
    # time(hour = 0, minute = 0, second = 0)
    t = Time(date= datetime.date(date),start_time= datetime.time(start_time),end_time= datetime.time(end_time))
    t.save()
    return t.time_id
    # zahra side


def append_mh_time(mh_id, time_id):  # append a mh_time and return its id
    mt = MH_Time(mh_id= mh_id,time_id=time_id)
    mt.save()
    return mt.id
    # zahra side

