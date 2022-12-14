import json

input = '''{ 
    "user_id":"ID",
     }'''

def Past_Meetings(user_id):
    # Database 
    pass

def Today_Meetings(user_id):
    # Database 
    pass

def Future_Meetings(user_id):
    # Database 
    pass



def user_timeline(input):

    input = json.loads(input)
    user_id = input['user_id']

    output = {
        'Past Meetings': Past_Meetings(user_id),
        'Today Meetings': Present_Meetings(user_id),
        'Future Meetings': Future_Meetings(user_id),
    }

    return json.dumps(output)