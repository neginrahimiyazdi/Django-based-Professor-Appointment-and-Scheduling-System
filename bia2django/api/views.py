from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from api.main_functions import register_user, register_mh, mh_fill_timetable, login, make_time_id, reserve_meeting
import json


def check_inputs(input, policy):
    if policy == 'api_register_user':
        if 'first_name' not in input: raise Exception("You must mention first name!")
        if 'last_name' not in input: raise Exception("You must mention last name!")
        if 'user_email' not in input: raise Exception("You must mention email!")
        if 'user_password' not in input: raise Exception("You must mention password!")
        elif len(input['user_password'])<8: raise Exception("Lenght of password must be at least 8!")
        if 'student_number' not in input: raise Exception("You must mention student number!")
        if 'mobile_number' not in input: raise Exception("You must mention mobile number!")
        if 'degree' not in input: input['degree']=''
        if 'field' not in input: input['field']=''
        if 'university' not in input: input['university']=''
        if 'adviserID' not in input: raise Exception("You must mention adviserID!")
    
    if policy == 'api_register_mh':
        if 'first_name' not in input: raise Exception("You must mention first name!")
        if 'last_name' not in input: raise Exception("You must mention last name!")
        if 'MH_email' not in input: raise Exception("You must mention email!")
        if 'MH_password' not in input: raise Exception("You must mention password!")
        elif len(input['MH_password'])<8: raise Exception("Lenght of password must be at least 8!")
        if 'teacher_number' not in input: input['teacher_number']=''
        if 'degree' not in input: input['degree']=''
        if 'field' not in input: input['field']=''
        if 'link_to_webpage' not in input: input['link_to_webpage']=''
    
    if policy == 'api_login':
        if 'email' not in input: raise Exception("You must mention email!")
        if 'password' not in input: raise Exception("You must mention password!")

    if policy == 'api_mh_fill_timetable':
        if 'mh_id' not in input: raise Exception("You must mention mh_id!")
        if 'days' not in input: raise Exception("You must mention days!")

    if policy == 'api_make_time_id':
        if 'date' not in input: raise Exception("You must mention date!")
        if 'start_time' not in input: raise Exception("You must mention start_time!")
        if 'end_time' not in input: raise Exception("You must mention end_time!")

    if policy == 'api_reserve_meeting':
        if 'mh_id' not in input: raise Exception("You must mention mh_id!")
        if 'user_id' not in input: raise Exception("You must mention user_id!")
        if 'time_id' not in input: raise Exception("You must mention user_id!")
        if 'subject' not in input: raise Exception("You must mention subject!")
        if 'rate' not in input: input['rate'] = -1
        if 'description' not in input: input['description'] = ""
        if 'was_holded' not in input: input['was_holded'] = False



        
    return input

succes = {"is_succesfull": True, "error_string": ""}
# API's list

def api_register_user(request): 
    '''
    This api registers a new user and returns it's ID.
    input: first_name, last_name, user_email, user_password, student_number, mobile_number, degree, field, university, adviserID
    output: user_id, is_succesfull, error_string
    input example: 
    {
        "first_name":"ali",
        "last_name":"rezaii",
        "user_email":"alir@gmail.com",
        "user_password":"12345678",
        "student_number":"0",
        "mobile_number":"0",
        "adviserID":5
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_register_user')
        output = register_user(input)
        output.update(succes)

    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e),}

    return JsonResponse(output)


def api_register_mh(request): 
    '''
    This api registers a new MH and returns it's ID.
    input: first_name, last_name, MH_email, MH_password, teacher_number, degree, field, link_to_webpage
    output: mh_id, is_succesfull, error_string
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_register_mh')
        output = register_mh(input)
        output.update(succes)

    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e),}

    return JsonResponse(output)


def api_login(request): 
    '''
    This api logins a user and returns it's ID (if logined).
    input: email, password
    output: role, person_id, is_succesfull, error_string
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_login')
        output = login(input)
        output.update(succes)

    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e),}

    return JsonResponse(output)

def api_mh_fill_timetable(request): 
    '''
    This api gets data's of a timetable (free times of an MH) and assigns it to an MH.
    input: mh_id, days
    output: role, person_id, is_succesfull, error_string
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_mh_fill_timetable')
        mh_fill_timetable(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_make_time_id(request):
    '''
    This api gets information of a time and makes time_id
    input: date, start_time, end_time
    output: is_succesfull, error_string
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_make_time_id')
        output = make_time_id(input)
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)
    
def api_reserve_meeting(request):
    '''
    This api gets an mh_id and user_id and sets a meeting between them.
    input: mh_id, user_id, time_id, subject, rate, description, was_holded
    output: is_succesfull, error_string
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_reserve_meeting')
        reserve_meeting(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)
    