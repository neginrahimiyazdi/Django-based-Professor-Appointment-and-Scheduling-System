# Used in: register_user
from api.orm_functions import get_role, add_user    
# Used in: register_mh                             
from api.orm_functions import get_role, add_mh  
# Used in: login                                 
from api.orm_functions import get_role, check_password, get_user_id   
# Used in: mh_fill_timetable
from api.orm_functions import remove_mh_day_meetings, append_time, append_mh_time


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
        remove_mh_day_meetings(mh_id, day['date']) 
        for mh_time in day['meetings']:
            time_id = append_time(day['date'], mh_time['start_time'], mh_time['end_time'])
            append_mh_time(mh_id, time_id)

