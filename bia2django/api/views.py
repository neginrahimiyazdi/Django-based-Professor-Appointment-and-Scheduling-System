from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from api.main_functions import register_user, register_mh, login
from api.main_functions import mh_fill_timetable, get_timetable
from api.main_functions import reserve_meeting, get_list_of_mh 
from api.main_functions import get_mh_timeline, get_user_timeline
from api.main_functions import get_mh_account, get_user_account
from api.main_functions import fill_mh_account, fill_user_account
from api.orm_functions import authenticate_person
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
        if 'mh_email' not in input: raise Exception("You must mention email!")
        if 'mh_password' not in input: raise Exception("You must mention password!")
        elif len(input['mh_password'])<8: raise Exception("Lenght of password must be at least 8!")
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
        if 'date' not in input: raise Exception("You must mention date!")
        if 'start_time' not in input: raise Exception("You must mention start_time!")
        if 'end_time' not in input: raise Exception("You must mention end_time!")
        if 'subject' not in input: raise Exception("You must mention subject!")
        if 'rate' not in input: input['rate'] = -1
        if 'description' not in input: input['description'] = ""
        if 'was_holded' not in input: input['was_holded'] = False

    if policy == 'api_get_timetable':
        if 'mh_id' not in input: raise Exception("You must mention mh_id!")
        if 'date' not in input: raise Exception("You must mention date!")
    
    if policy == 'api_mh_timeline':
        if 'mh_id' not in input: raise Exception("You must mention mh_id!")
        if 'date' not in input: raise Exception("You must mention date!")
    
    if policy == 'api_user_timeline':
        if 'user_id' not in input: raise Exception("You must mention user_id!")
        if 'date' not in input: raise Exception("You must mention date!")
    
    if policy == "get_mh_account":
        if 'mh_id' not in input: raise Exception("You must mention mh_id!")
    
    if policy == "get_user_account":
        if 'user_id' not in input: raise Exception("You must mention user_id!")
    
    return input

succes = {"is_succesfull": True, "error_string": ""}
# API's list


def api_register_mh(request): 
    '''
    This api registers a new mh and returns it's ID.
    input: first_name, last_name, mh_email, mh_password, teacher_number, degree, field, link_to_webpage
    output: mh_id, is_succesfull, error_string
    api url: [host_address]/api/register_mh/
    access level: public
    input example: 
    {
        "first_name": "Luke",
        "last_name": "Bryan",
        "mh_email": "LukeB@gmaiil.com",
        "mh_password": "87654321",
        "teacher_number": "0",
        "degree": "Full Teacher",
        "field": "Country",
        "link_to_webpage": ""
    }
    output example:
    {
        "mh_id": 1,
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_register_mh')
        output = register_mh(input)
        output.update(succes)

    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e),}

    return JsonResponse(output)

def api_register_user(request): 
    '''
    This api registers a new user and returns it's ID.
    input: first_name, last_name, user_email, user_password, student_number, mobile_number, degree, field, university, adviserID
    output: user_id, is_succesfull, error_string
    api url: [host_address]/api/register_user/
    access level: public
    input example: 
    {
        "first_name":"Isaac",
        "last_name":"Newton",
        "user_email":"IsaacN@gmail.com",
        "user_password":"87654321",
        "student_number":"0",
        "mobile_number":"0",
        "adviserID":1,
        "degree":"Diploma",
        "field":"Physic",
        "university":"Amirkabir"
    }
    output example:
    {
        "user_id": 1,
        "is_succesfull": true,
        "error_string": ""
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

def api_login(request): 
    '''
    This api logins a user and returns it's ID (if logined).
    input: email, password
    output: role, person_id, is_succesfull, error_string
    api url: [host_address]/api/login/
    access level: only the email owner - you need to provide the password that is assigned to the email
    input example: 
    {
        "email":"IsaacN@gmail.com",
        "password":"87654321"
    }
    output example:
    {
        "role": "user",
        "person_id": 1,
        "is_succesfull": true,
        "error_string": ""
    }
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
    This api gets data's of a timetable (free times of an mh) and assigns it to an mh.
    input: mh_id, mh_password, days
    output: is_succesfull, error_string
    api url: [host_address]/api/mh_fill_timetable/
    access level: only the meeting holder - you need to provide the mh_password that is assigned to the mh
    input example: 
    {
        "mh_id": "1",
        "mh_password":"87654321",
        "days": [
            {
                "date": {"year":2022, "month":12, "day":8},
                "meetings": [
                    {
                        "start_time": {"hour":12, "minute":30, "second":0},
                        "end_time": {"hour":13, "minute":30, "second":0}
                    }
                ]
            },
            {
                "date": {"year":2022, "month":12, "day":9},
                "meetings": [
                    {
                        "start_time": {"hour":14, "minute":30, "second":0},
                        "end_time": {"hour":15, "minute":30, "second":0}
                    }
                ]
            }
        ]
    }
    output example:
    {
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_mh_fill_timetable')
        authenticate_person(input['mh_id'], "mh", input['mh_password'])
        mh_fill_timetable(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_get_list_of_mh(request):
    '''
    This api returns list of all mh's
    input: _
    output: mh_list, is_succesfull, error_string
    api url: [host_address]/api/get_list_of_mh/
    access level: public
    input example: {}
    output example:
    {
        "mh_list": [
            {
                "id": 1,
                "first_name": "Luke",
                "last_name": "Bryan",
                "mh_email": "LukeB@gmaiil.com",
                "degree": "Full Teacher",
                "field": "Country",
                "link_to_webpage": ""
            }
        ],
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        output = get_list_of_mh()
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_reserve_meeting(request):
    '''
    This api gets an mh_id and user_id and sets a meeting between them.
    input: mh_id, user_id, user_password, date, start_time, end_time, subject, rate, description, was_holded
    output: is_succesfull, error_string
    api url: [host_address]/api/reserve_meeting/
    access level: only the user - you need to provide the user_password that is assigned to the user
    input example: 
    {
        "mh_id": 1,
        "user_id": 1,
        "user_password": "87654321",
        "date": {"year": 2022, "month": 12, "day": 8},
        "start_time": {"hour": 12, "minute": 45, "second": 0},
        "end_time": {"hour": 13, "minute": 15, "second": 0},
        "subject": "saying hello",
        "rate": -1,
        "description": "nothing",
        "was_holded": false
    }
    output example:
    {
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_reserve_meeting')
        authenticate_person(input['user_id'], "user", input['user_password'])
        reserve_meeting(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)
    
def api_get_timetable(request):
    '''
    This api gets an mh_id and a date and returns timetable of whole week that includes the day.
    input: mh_id, date
    output: mh_id, days[7]
    api url: [host_address]/api/get_timetable/
    access level: public
    input example: 
    {
        "mh_id": 1,
        "date": {"year":2022, "month":12, "day":8}
    }
    output example:
    {
        "mh_id": 1,
        "days": [
            {
                "date": {"year": 2022, "month": 12, "day": 3},
                "meetings": []
            },
            {
                "date": {"year": 2022, "month": 12, "day": 4},
                "meetings": []
            },
            {
                "date": {"year": 2022, "month": 12, "day": 5},
                "meetings": []
            },
            {
                "date": {"year": 2022, "month": 12, "day": 6},
                "meetings": []
            },
            {
                "date": {"year": 2022, "month": 12, "day": 7},
                "meetings": []
            },
            {
                "date": {"year": 2022, "month": 12, "day": 8},
                "meetings": [
                    {
                        "start_time": {"hour": 13, "minute": 15, "second": 0},
                        "end_time": {"hour": 13, "minute": 30, "second": 0}
                    },
                    {
                        "start_time": {"hour": 12, "minute": 30, "second": 0},
                        "end_time": {"hour": 12, "minute": 45, "second": 0}
                    }
                ]
            },
            {
                "date": {"year": 2022, "month": 12, "day": 9},
                "meetings": [
                    {
                        "start_time": {"hour": 14, "minute": 30, "second": 0},
                        "end_time": {"hour": 15, "minute": 30, "second": 0}
                    }
                ]
            }
        ],
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_get_timetaible')
        output = get_timetable(input)
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_get_mh_timeline(request):
    '''
    This api gets an mh_id and a date (today date) and returns the meetings that the person has.
    input: mh_id, mh_password, date
    output: past_meetings, present_meetings, future_meetings, is_succesfull, error_string
    api url: [host_address]/api/get_mh_timeline/
    access level: only the meeting holder - you need to provide the mh_password that is assigned to the mh
    input example: 
    {
        "mh_id": 1,
        "mh_password": "87654321",
        "date": {"year":2022, "month":12, "day":9}
    }
    output example:
    {
        "past_meetings": [
            {
                "meeting_id": 1,
                "user_first_name": "Isaac",
                "user_last_name": "Newton",
                "date": "2022-12-08",
                "start_time": "12:45:00",
                "end_time": "13:15:00"
            }
        ],
        "present_meetings": [],
        "future_meetings": [],
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_get_mh_timeline')
        authenticate_person(input['mh_id'], "mh", input['mh_password'])
        output = get_mh_timeline(input)
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_get_user_timeline(request):
    '''
    This api gets an user_id and a date (today date) and returns the meetings that the person has.
    input: user_id, user_password, date
    output: past_meetings, present_meetings, future_meetings, is_succesfull, error_string
    api url: [host_address]/api/get_user_timeline/
    access level: only the user - you need to provide the user_password that is assigned to the user
    input example: 
    {
        "user_id": 1,
        "user_password":"87654321",
        "date": {"year":2022, "month":12, "day":9}
    }
    output example:
    {
        "past_meetings": [
            {
                "meeting_id": 1,
                "mh_first_name": "Luke",
                "mh_last_name": "Bryan",
                "date": "2022-12-08",
                "start_time": "12:45:00",
                "end_time": "13:15:00"
            }
        ],
        "present_meetings": [],
        "future_meetings": [],
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'api_get_user_timeline')
        authenticate_person(input['user_id'], "user", input['user_password'])
        output = get_user_timeline(input)
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_get_mh_account(request):
    '''
    This api gets an mh_id and returns information of the user.
    input: mh_id, mh_password
    output: first_name, last_name, mh_email, mh_password, teacher_number, degree, field, link_to_webpage, is_succesfull, error_string
    api url: [host_address]/api/get_mh_account/
    access level: only the meeting holder - you need to provide the mh_password that is assigned to the mh
    input example: 
    {
        "mh_id": 1,
        "mh_password":"87654321"
    }
    output example:
    {
        "first_name": "Luke",
        "last_name": "Bryan",
        "mh_email": "LukeB@gmaiil.com",
        "mh_password": "87654321",
        "teacher_number": "0",
        "degree": "Full Teacher",
        "field": "Country",
        "link_to_webpage": "",
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'get_mh_account')
        authenticate_person(input['mh_id'], "mh", input['mh_password'])
        output = get_mh_account(input)
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_get_user_account(request):
    '''
    This api gets an mh_id and returns information of the user.
    input: user_id, user_password
    output: first_name, last_name, user_email, user_password, student_number, mobile_number, degree, field, university, adviserID, is_succesfull, error_string
    api url: [host_address]/api/get_user_account/
    access level: only the user - you need to provide the user_password that is assigned to the user
    input example: 
    {
        "user_id": 1,
        "user_password":"87654321"
    }
    output example:
    {
        "first_name": "Isaac",
        "last_name": "Newton",
        "user_email": "IsaacN@gmail.com",
        "user_password": "87654321",
        "student_number": "0",
        "mobile_number": "0",
        "degree": "Diploma",
        "field": "Physic",
        "university": "Amirkabir",
        "adviserID": 1,
        "is_succesfull": true,
        "error_string": ""
    }
    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'get_user_account')
        authenticate_person(input['user_id'], "user", input['user_password'])
        output = get_user_account(input)
        output.update(succes)
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)






def api_fill_mh_account(request):
    '''
    This api gets an mh_id and information of the mh and updates it.
    input: mh_id, mh_password, first_name, last_name, mh_email, mh_password, teacher_number, degree, field, link_to_webpage
    output: is_succesfull, error_string
    api url: [host_address]/api/fill_mh_account/
    access level: only the meeting holder - you need to provide the mh_password that is assigned to the mh
    input example: 

    output example:

    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'fill_mh_account')
        authenticate_person(input['mh_id'], "mh", input['mh_password'])
        fill_mh_account(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)

def api_fill_user_account(request):
    '''
    This api gets an user_id and information of the mh and updates it.
    input: user_id, user_email, first_name, last_name, user_password, student_number, mobile_number, degree, field, university, adviserID, is_succesfull, error_string
    output: is_succesfull, error_string
    api url: [host_address]/api/fill_user_account/
    access level: only the user - you need to provide the user_password that is assigned to the user
    input example: 

    output example:

    '''
    try:
        input = json.loads(request.body) 
        input = check_inputs(input, 'fill_user_account')
        authenticate_person(input['user_id'], "user", input['user_password'])
        fill_user_account(input)
        output = succes.copy()
    except Exception as e:
        output = {"is_succesfull": False, "error_string": str(e)}

    return JsonResponse(output)





