import json

def change_info(mh_id, info):
    #database side
    pass



input = '''{ 
    "mh_id":"ID",
    "info": "new information that you want to change" , 
        }'''
        
def fill_mh_account(input): 

    # edit the account information
    # read the information from mh and front
    # change the information in database 

    # I'm not sure but
    # zahra
    # ali

    # if mh not found : Error
    # if information are not acceptable : Error
    # else : modified account sucessfuly

    try: 
        input = json.loads(input)
        mh_id, info = input['mh_id'], input['info']
        change_info('mh_id', 'info')

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
        
