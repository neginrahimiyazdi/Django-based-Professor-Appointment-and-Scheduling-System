#functions for mh_fill_timetable API

import datetime
from api.models import Time,User,MH,Meeting,MH_Time

def check_equality(pass1, pass2):
    return pass1==pass2

def authenticate_person(person_id, role, password):
    if role=='user':
        queryset = User.objects.filter(id=person_id).values('user_password')
        if queryset.count()==0:
            raise Exception("user_id doesn\'t exist in database.")
        if not check_equality(queryset[0]['user_password'], password):
            raise Exception("Password is incorrect!")
    elif role=='mh':
        queryset = MH.objects.filter(id=person_id).values('mh_password')
        if queryset.count()==0:
            raise Exception("mh_id doesn\'t exist in database.")
        if not check_equality(queryset[0]['mh_password'], password):
            raise Exception("Password is incorrect!")

def add_user(first_name, last_name, user_email, user_password, student_number, mobile_number, degree, field, university, adviserID):
    
    user = User(first_name=first_name, last_name=last_name, 
                user_email=user_email, user_password=user_password, 
                student_number=student_number, mobile_number=mobile_number, 
                degree=degree, field=field, 
                university=university, adviserID_id=adviserID)
    user.save()   
    return user.id

    
def add_mh(first_name, last_name, mh_email, mh_password, teacher_number, degree, field, link_to_webpage):
    mh = MH(first_name=first_name, last_name=last_name, 
            mh_email=mh_email, mh_password=mh_password, 
            teacher_number=teacher_number, degree=degree, 
            field=field, link_to_webpage=link_to_webpage)
    mh.save()  
    return mh.id



def remove__times(mh_id, date):  # remove * from meetings where mh_id={} and date={}
    times = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day'])).values('id')
    for time in times:
        record = MH_Time.objects.filter(mhID_id = mh_id , timeID_id= time['id'])
        if record.count()>0: record.delete()


def remove_mh_times(mh_id, date):  # remove * from meetings where mh_id={} and date={}
    times = Time.objects.filter(date=datetime.date(date['year'], date['month'], date['day'])).values('id')
    for time in times:
        record = MH_Time.objects.filter(mhID_id = mh_id , timeID_id= time['id'])
        if record.count()>0: record.delete()

        
def append_time(date, start_time, end_time):  # append a time and return its id
    # date(year = 0, month = 0, day = 0)
    # time(hour = 0, minute = 0, second = 0)
    if type(date) is not datetime.date: date = datetime.date(date['year'], date['month'], date['day'])
    if type(start_time) is not datetime.time: start_time= datetime.time(start_time['hour'], start_time['minute'], start_time['second'])
    if type(end_time) is not datetime.time: end_time= datetime.time(end_time['hour'], end_time['minute'], end_time['second'])
    
    queryset = Time.objects.filter(date=date,start_time=start_time,end_time=end_time)
    if queryset.count()>0: return queryset.values('id')[0]['id']
    time = Time(date=date,start_time=start_time,end_time=end_time)
    time.save()
    return time.id
    # zahra side


def append_mh_time(mh_id, time_id):  # append a mh_time and return its id
    mt = MH_Time(mhID_id= mh_id, timeID_id=time_id)
    mt.save()
    return mt.id
    # zahra side

def get_role(email):   #if user exists return True , else return False
    queryset1 = User.objects.filter(user_email=email).count()
    queryset2 = MH.objects.filter(mh_email=email).count()
    if queryset1 > 0: return 'user'
    if queryset2 > 0: return 'mh'
    else: return None

def check_password(email, role, password):    #if user password was wrong return False
    if role=='user': queryset = User.objects.filter(user_email= email).values('user_password')[0]['user_password']
    elif role=='mh': queryset = MH.objects.filter(mh_email= email).values('mh_password')[0]['mh_password']
    return check_equality(queryset, password)

def get_user_id(email, role):
    if role=='user': queryset = User.objects.filter(user_email= email).values('id')[0]['id']
    elif role=='mh': queryset = MH.objects.filter(mh_email= email).values('id')[0]['id']
    return queryset


####################################
#functions for user_account API

def user_information(user_id): #return user info from database
    #Database
    queryset = User.objects.filter(user_id= user_id)
    return queryset


def append_meeting(mh_id, time_id, user_id, subject,rate, was_holded, description): #reserve meeting
    m = Meeting(subject= subject, rate=rate, was_holded=was_holded,description= description, mhID_id= mh_id, userID_id= user_id, timeID_id= time_id)
    m.save()
    return m.id  # zahra side

def get_mh_list():
    return list(MH.objects.values('id', 'first_name', 'last_name', 'mh_email', 'degree', 'field', 'link_to_webpage'))


def remove_time_from_mh_times(mh_id, date, start_time, end_time):
    date = datetime.date(year=date["year"], month=date["month"], day=date["day"])
    start_time = datetime.time(hour=start_time['hour'], minute=start_time['minute'], second=start_time['second'])
    end_time = datetime.time(hour=end_time['hour'], minute=end_time['minute'], second=end_time['second'])
    queryset = MH_Time.objects.filter(mhID_id=mh_id).values('timeID')
    print(queryset)
    for timeID in queryset:
        time = Time.objects.filter(id=timeID['timeID']).values("start_time", "end_time", "date")[0]
        
        if time["date"] != date:
            continue
        if start_time >= time["start_time"] and end_time <= time["end_time"]:
            if end_time != time["end_time"]:
                time_id = append_time(date, end_time, time["end_time"])
                append_mh_time(mh_id, time_id)
            if time["start_time"] != start_time:
                time_id = append_time(date, time["start_time"], start_time)
                append_mh_time(mh_id, time_id)
            record = MH_Time.objects.filter(mhID_id=mh_id, timeID_id=timeID['timeID'])
            record.delete()
            return
    raise Exception("mh is not available in this time!")


def get_mh_times(mh_id, date):
    mh_times = []
    times = Time.objects.filter(date=date).values('id', 'date', 'start_time', 'end_time')
    for time in times:
        record = MH_Time.objects.filter(mhID_id = mh_id , timeID_id= time['id'])
        if record.count()>0:
            
            start_time, end_time = time['start_time'], time['end_time']
            mh_times.append({ "start_time": {"hour":start_time.hour, "minute":start_time.minute, "second":start_time.second},
                                "end_time": {"hour":end_time.hour, "minute":end_time.minute, "second":end_time.second}})
    return mh_times




def mh_meetings(mh_id, date, order): 
    if type(date) is not datetime.date: date = datetime.date(date['year'], date['month'], date['day'])
    output = []
    times = Time.objects.filter().values('id', 'date', 'start_time', 'end_time')
    for time in times:
        if (order=='past' and time['date']<date) or (order=='present' and time['date']==date) or (order=='future' and time['date']>date):
            meets = Meeting.objects.filter(mhID_id=mh_id, timeID_id=time['id']).values('id', 'userID')
            for meet in meets:
                user = User.objects.filter(id=meet['userID']).values('first_name', 'last_name')[0]
                output.append({'meeting_id':meet['id'], 
                               'user_first_name':user['first_name'],
                               'user_last_name':user['last_name'],
                               'date':time['date'],
                               'start_time':time['start_time'],
                               'end_time':time['end_time']})
    return output


def user_meetings(user_id, date, order): 
    if type(date) is not datetime.date: date = datetime.date(date['year'], date['month'], date['day'])
    output = []
    times = Time.objects.filter().values('id', 'date', 'start_time', 'end_time')
    for time in times:
        if (order=='past' and time['date']<date) or (order=='present' and time['date']==date) or (order=='future' and time['date']>date):
            meets = Meeting.objects.filter(userID_id=user_id, timeID_id=time['id']).values('id', 'mhID')
            for meet in meets:
                mh = MH.objects.filter(id=meet['mhID']).values('first_name', 'last_name')[0]
                output.append({'meeting_id':meet['id'], 
                               'mh_first_name':mh['first_name'],
                               'mh_last_name':mh['last_name'],
                               'date':time['date'],
                               'start_time':time['start_time'],
                               'end_time':time['end_time']})
    return output





def get_account(person_id, role):
    if role=='user':
        queryset = User.objects.filter(id=person_id).values('first_name', 'last_name', 'user_email', 
                                                            'user_password', 'student_number', 
                                                            'mobile_number', 'degree', 'field', 
                                                            'university', 'adviserID')
        if queryset.count()>0:
            return queryset[0]
        else:
            raise Exception('user_id doesn\'t exist in database!')
    elif role=='mh':
        queryset = MH.objects.filter(id=person_id).values('first_name', 'last_name', 'mh_email', 
                                                            'mh_password', 'teacher_number', 
                                                            'degree', 'field', 'link_to_webpage')
        if queryset.count()>0:
            return queryset[0]
        else:
            raise Exception('mh_id doesn\'t exist in database!')

def set_account(person_id, role, input):
    if role=='mh':
        mh = MH.objects.filter(id=person_id)[0]
        mh.first_name, mh.last_name = input['first_name'], input['last_name']
        mh.mh_email, mh.mh_password = input['mh_email'], input['mh_password']
        mh.teacher_number, mh.degree = input['teacher_number'], input['degree']
        mh.field, mh.link_to_webpage = input['field'], input['link_to_webpage']
        mh.save()
    if role=='user':
        user = User.objects.filter(id=person_id)[0]
        user.first_name, user.last_name = input['first_name'], input['last_name']
        user.user_email, user.user_password = input['user_email'], input['user_password']
        user.student_number, user.mobile_number = input['student_number'], input['mobile_number']
        user.degree, user.field = input['degree'], input['field']
        user.university = input['university']
        user.save()