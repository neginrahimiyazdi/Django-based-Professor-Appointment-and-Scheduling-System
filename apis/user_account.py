import json

def information(user_id): 
    # return the information of user from database
    # database side
    # zahra
    # return information
    pass


input = '''{ 
    "user_id":"ID",
        }'''


# Question?
# is user_id same as username in login.py
# if so the user id is same as the email of user

def user_account(input):

    input = json.loads(input)
    user_id = input['user_id']
    return information(user_id)