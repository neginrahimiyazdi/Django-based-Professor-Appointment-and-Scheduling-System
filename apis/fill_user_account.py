import json

def change_info(user_id, info):
    #database side
    pass



input = '''{ 
    "user_id":"ID",
    "info": "new information that you want to change" , 
        }'''
        
def fill_user_account(input): 

    # edit the accountinformation
    # read the information from user and front
    # change the information in database 

    # I'm not sure but
    # zahra
    # ali

    # if user not found : Error
    # if information are not acceptable : Error
    # else : modified account sucessfuly

    try: 
        input = json.loads(input)
        user_id, info = input['user_id'], input['info']
        change_info('user_id', 'info')

        output = {
            'is_successful': True, 
            'error_string': '',
        }
        
        return json.dumps(output)

    except Exception as e:
        output = {
            'is_successful': False, 
            'error_string': str(e),
        }
        return json.dumps(output)
        





