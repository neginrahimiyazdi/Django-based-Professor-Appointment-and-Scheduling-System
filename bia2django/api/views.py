from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from api.main_functions import register_user, register_mh, mh_fill_timetable, login
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
    
    return input

succes = {"is_succesfull": True, "error_string": ""}
# API's list

def api_register_user(request): 
    '''
    This api registers a new user and returns it's ID.
    input: first_name, last_name, user_email, user_password, student_number, mobile_number, degree, field, university, adviserID
    output: user_id, is_succesfull, error_string
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
    try:
        input = json.loads(request.body) 
        mh_fill_timetable(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

