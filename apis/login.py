# follow up codes

# in main -> urls 
#   from django.contrib.auth import views as auth_views
#   add:
#   path('login/', auth_views.LoginView.as_view(), name='Login'),
#   path('logout/', auth_views.LogoutView.as_view(), name='logout'),

# Note: after login sucessfuly go to the setting.py and
# add:
#   LOGIN_REDIRECT_URL = 'blog-home'

# Note: We need log out too, because of security problem!
# When you login the user can access admin!

import json

def check_user_id(username):
    # Database side
    # if user not exist return proper action
    pass

def check_password(username, password):
    # Database side
    # if user password was wrong return proper action
    pass


input = '''{ 
    "username":"abolfazlansari@aut.ac.ir",
    "password":"Icannontsharemypass",
        }'''


def login(input):

    try:
        input = json.loads(input)
        username, password = input['username'], input['password']
        check_user_id(username)
        check_password(username, password)

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




