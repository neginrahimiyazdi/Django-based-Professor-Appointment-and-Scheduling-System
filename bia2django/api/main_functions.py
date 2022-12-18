# Used in: register_user
from api.orm_functions import get_role, add_user    
# Used in: register_mh                             
from api.orm_functions import get_role, add_mh  
# Used in: login                                 
from api.orm_functions import get_role, check_password, get_user_id   
# Used in: mh_fill_timetable
from api.orm_functions import remove_mh_times, append_time, append_mh_time
# Used in: get_list_of_mh
from api.orm_functions import get_mh_list
# Used in: reserve_meeting
from api.orm_functions import append_time, remove_time_from_mh_times, append_meeting
# Used in: get_timetaible
from api.orm_functions import get_mh_times
# Used in: 
from api.orm_functions import mh_meetings

import datetime

def register_user(input):
    if get_role(input['user_email']) != None:
        raise Exception('Email already exists!')
    user_id = add_user(input['first_name'], input['last_name'], 
                       input['user_email'], input['user_password'], 
                       input['student_number'], input['mobile_number'],  
                       input['degree'], input['field'], 
                       input['university'], input['adviserID'])
    output = {"user_id": user_id}
    return output

def register_mh(input):
    if get_role(input['MH_email']) != None:
        raise Exception('Email already exists!')
    user_id = add_mh(input['first_name'], input['last_name'], 
                     input['MH_email'], input['MH_password'], 
                     input['teacher_number'], input['degree'], 
                     input['field'], input['link_to_webpage'])
    output = {"mh_id": user_id}
    return output

def login(input):
    role = get_role(input['email'])
    if role==None: 
        raise Exception("Email doesn't exist!")
    if not check_password(input['email'], role, input['password']):
        raise Exception("Password is wrong!")
    person_id = get_user_id(input['email'], role)
    output = {"role":role, "person_id": person_id}
    return output

def mh_fill_timetable(input):
    mh_id, days = input['mh_id'], input['days']
    for day in days:
        remove_mh_times(mh_id, day['date']) 
        for mh_time in day['meetings']:
            time_id = append_time(day['date'], mh_time['start_time'], mh_time['end_time'])
            append_mh_time(mh_id, time_id)

def get_list_of_mh():
    mh_list = get_mh_list()
    return {"mh_list":mh_list}
    
def reserve_meeting(input):
    time_id = append_time(input["date"], input["start_time"], input["end_time"])
    remove_time_from_mh_times(input["mh_id"], input["date"], input["start_time"], input["end_time"])
    meeting_id = append_meeting(input["mh_id"],  time_id,
                                input["user_id"], input["subject"], 
                                input["rate"], input["was_holded"],
                                input["description"])
    return meeting_id

def get_timetaible(input):
    output = {'mh_id':input['mh_id'], 'days':[]}
    date = datetime.date(input['date']['year'], input['date']['month'], input['date']['day'])
    saturday_date = date + datetime.timedelta(-((date.weekday()+2)%7))
    for i in range(7):
        i_day = saturday_date + datetime.timedelta(i)
        day = {'date':{"year":i_day.year, "month":i_day.month, "day":i_day.day},
               'meetings': get_mh_times(input['mh_id'], i_day)}
        output['days'].append(day)
    return output
        
def mh_timeline(input):
    output = {
        'past_meetings':mh_meetings(input['mh_id'], input['date'], 'past'),
        'present_meetings':mh_meetings(input['mh_id'], input['date'], 'present'),
        'future_meetings':mh_meetings(input['mh_id'], input['date'], 'future'),
    }
    return output