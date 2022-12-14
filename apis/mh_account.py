import json

def information(mh_id): 
    # return the information of meeting holder from database
    # database side
    # zahra
    # return information
    pass


input = '''{ 
    "mh_id":"ID",
        }'''



def mh_account(input):

    input = json.loads(input)
    mh_id = input['mh_id']
    return information(mh_id)