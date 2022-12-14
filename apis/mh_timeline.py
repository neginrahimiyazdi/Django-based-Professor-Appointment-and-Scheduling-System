import json

input = '''{ 
    "mh_id":"ID",
     }'''

def Past_Meetings(mh_id):
    # Database 
    pass

def Today_Meetings(mh_id):
    # Database 
    pass

def Future_Meetings(mh_id):
    # Database 
    pass



def user_timeline(input):

    input = json.loads(input)
    user_id = input['mh_id']

    output = {
        'Past Meetings': Past_Meetings(mh_id),
        'Today Meetings': Present_Meetings(mh_id),
        'Future Meetings': Future_Meetings(mh_id),
    }

    return json.dumps(output)