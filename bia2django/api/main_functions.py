from api.orm_functions import add_user, add_mh
from api.orm_functions import get_role, check_password, get_user_id
from api.orm_functions import remove_mh_day_meetings, append_time, append_mh_time

import json

input = '''{ 
    "mh_id":"123", 
    "days":[{"date":"12/08/2022", "meetings":[{"start_time":"12:30", "end_time"="13:30"}, {"start_time":"17:30", "end_time"="18:30"}]}
           ,{"date":"12/09/2022", "meetings":[{"start_time":"14:30", "end_time"="15:30"}]}
          ]}
        '''

def register_user(input):
    user_id = add_user(input['first_name'], input['last_name'], 
                   input['user_email'], input['user_password'], 
                   input['student_number'], input['mobile_number'],  
                   input['degree'], input['field'], 
                   input['university'], input['adviserID'])
    output = {"user_id": user_id}
    return output

def register_mh(input):
    user_id = add_user(input['first_name '], input['last_name'], 
                     input['user_email'], input['user_password'], 
                     input['student_number'], input['mobile_number'], 
                     input['degree'], input['field'], 
                     input['university'], input['adviserID'])
    output = {"user_id": user_id}
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

