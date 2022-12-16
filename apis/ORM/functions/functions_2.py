import datetime
from testdb.models import Time,User,MH,Meeting,MH_Time
from datetime import datetime, timedelta
####################################
#functions for user_timeline API

def user_Past_Meetings(user_id): #return meeting_id
    # Database
    x = datetime.now() - timedelta(1)
    previous_day = x.date()
    ??queryset_1 = Time.objects.filter(date=datetime.date(previous_day)).values('time_id')
    queryset_2 = Meeting.objects.filter(user_id= user_id, time_id= queryset_1).values('meeting_id')
    return queryset_2

def user_Today_Meetings(user_id): #return meeting_id
    # Database
    today = datetime.date.today()
    queryset_1 = Time.objects.filter(date=datetime.date(today)).values('time_id')
    queryset_2 = Meeting.objects.filter(user_id= user_id, time_id= queryset_1).values('meeting_id')
    return queryset_2

def user_Future_Meetings(user_id):
    # Database
    x = datetime.now() + timedelta(1)
    tomorrow = x.date()
    ??queryset_1 = Time.objects.filter(date=datetime.date(tomorrow)).values('time_id')
    queryset_2 = Meeting.objects.filter(user_id= user_id, time_id= queryset_1).values('meeting_id')
    return queryset_2

####################################
#functions for login API

def check_user_id(username):   #if user exists return True , else return False
    #Database
    #        username =  user email
    queryset = User.objects.filter(user_email=username).count()
    if (queryset == 0):
        print("user does not exist.")
        return  False
    else:
        return True

def check_password(username, password):    #if user password was wrong return False
    #Database
    queryset = User.objects.filter(user_email= username).values('user_password')
    if(queryset == password):
        return True
    else:
        return False

####################################
#functions for user_account API

def user_information(user_id): #return user info from database
    #Database
    queryset = User.objects.filter(user_id= user_id)
    return queryset

####################################
#??functions for fill_user_account API
??
def change_user_info(user_id, info, attribute):
    #Database

    pass

####################################
#functions for mh_account API

def MH_information(MH_id): #return MH info from database
    #Database
    queryset = MH.objects.filter(MH_id= MH_id)
    return queryset

####################################
#??functions for fill_mh_account API
??
def change_MH_info(MH_id, info, attribute):
    # Database

    pass

####################################
#functions for mh_timeline API

def mh_Past_Meetings(mh_id): #return meeting_id
    # Database
    x = datetime.now() - timedelta(1)
    previous_day = x.date()
    ??queryset_1 = Time.objects.filter(date=datetime.date(previous_day)).values('time_id')
    queryset_2 = Meeting.objects.filter(MH_id= mh_id, time_id= queryset_1).values('meeting_id')
    return queryset_2

def mh_Today_Meetings(mh_id): #return meeting_id
    # Database
    today = datetime.date.today()
    queryset_1 = Time.objects.filter(date=datetime.date(today)).values('time_id')
    queryset_2 = Meeting.objects.filter(MH_id= mh_id, time_id= queryset_1).values('meeting_id')
    return queryset_2

def mh_Future_Meetings(mh_id):
    # Database
    x = datetime.now() + timedelta(1)
    tomorrow = x.date()
    ??queryset_1 = Time.objects.filter(date=datetime.date(tomorrow)).values('time_id')
    queryset_2 = Meeting.objects.filter(MH_id= mh_id, time_id= queryset_1).values('meeting_id')
    return queryset_2


