#functions for mh_fill_timetable API

import datetime
from api.models import Time,User,MH,Meeting,MH_Time


def add_user(first_name, last_name, user_email, user_password, student_number, mobile_number, degree, field, university, adviserID):
    
    user = User(first_name=first_name, last_name=last_name, 
                user_email=user_email, user_password=user_password, 
                student_number=student_number, mobile_number=mobile_number, 
                degree=degree, field=field, 
                university=university, adviserID_id=adviserID)
    user.save()   
    return user.id

    
def add_mh(first_name, last_name, MH_email, MH_password, teacher_number, degree, field, link_to_webpage):
    mh = MH(first_name=first_name, last_name=last_name, 
            MH_email=MH_email, MH_password=MH_password, 
            teacher_number=teacher_number, degree=degree, 
            field=field, link_to_webpage=link_to_webpage)
    print([first_name, last_name, MH_email, MH_password, teacher_number, degree, field, link_to_webpage]) 
    mh.save()  
    
    return mh.id



def remove_mh_day_meetings(mh_id, date):  # remove * from meetings where mh_id={} and date={}
    time = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day'])).values('id')
    try :
        records = Meeting.objects.get(MHID_id = mh_id , timeID_id= time)
        records.delete()
        print("Records deleted successfully!")
    except Exception as e:
        print("Records doesn't exist : ", str(e))
    pass  # zahra side


def append_time(date, start_time, end_time):  # append a time and return its id
    # date(year = 0, month = 0, day = 0)
    # time(hour = 0, minute = 0, second = 0)
    time = Time(date= datetime.date(date['year'], date['month'], date['day']),
             start_time= datetime.time(start_time['hour'], start_time['minute'], start_time['second']),
             end_time= datetime.time(end_time['hour'], end_time['minute'], end_time['second']))
    time.save()
    return time.id
    # zahra side


def append_mh_time(mh_id, time_id):  # append a mh_time and return its id
    mt = MH_Time(MHID_id= mh_id, timeID_id=time_id)
    mt.save()
    return mt.id
    # zahra side


####################################
#functions for login API

def get_role(email):   #if user exists return True , else return False
    queryset1 = User.objects.filter(user_email=email).count()
    queryset2 = MH.objects.filter(MH_email=email).count()
    if queryset1 > 0: return 'user'
    if queryset2 > 0: return 'MH'
    else: return None

def check_password(email, role, password):    #if user password was wrong return False
    if role=='user': queryset = User.objects.filter(user_email= email).values('user_password')[0]['user_password']
    elif role=='MH': queryset = MH.objects.filter(MH_email= email).values('MH_password')[0]['MH_password']
    return queryset == password

def get_user_id(email, role):
    if role=='user': queryset = User.objects.filter(user_email= email).values('id')[0]['id']
    elif role=='MH': queryset = MH.objects.filter(MH_email= email).values('id')[0]['id']
    return queryset


####################################
#functions for user_account API

def user_information(user_id): #return user info from database
    #Database
    queryset = User.objects.filter(user_id= user_id)
    return queryset


####################################
#functions for mh_get_time_table API

def show_mh_day_meetings(mh_id, date): #select * from meeting where mh_id={} and date={}
    queryset_1 = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day'])).values('time_id')
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
    queryset_1 = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day'])).values('time_id')
    queryset_2 = MH_Time.objects.filter(MH_id= mh_id, time_id= queryset_1)
    return queryset_2
    # zahra side


def remove_mh_available_time(mh_id, date, start_time, end_time):
    queryset_1 = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day']), 
                start_time= datetime.time(start_time['hour'],start_time['minute'], start_time['second']), 
                end_time= datetime.time(end_time['hour'],end_time['minute'], end_time['second'])).values('time_id')
    queryset_2 = MH_Time.objects.filter(MH_id= mh_id, time_id= queryset_1)
    return queryset_2
    # zahra side

def append_meeting(mh_id, date, start_time, end_time, user_id, subject, description): #reserve meeting
    queryset_1 = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day']), 
                start_time=datetime.time(start_time['hour'],start_time['minute'], start_time['second']), 
                end_time=datetime.time(end_time['hour'],end_time['minute'], end_time['second'])).values('time_id')
    m = Meeting(subject= subject, description= description, MH_id= mh_id, user_id= user_id, time_id= queryset_1)
    m.save()
    pass  # zahra side










