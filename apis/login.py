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

from django.contrib.auth import views as auth_views
import json


# Database side
def get_password(username:'str'):
    # Send username to database
    if (user_not_found_in_database):
        return 'username not found!'
        #It could be a good idea to redirect register 
    else:
        return password


input = '''{ 
    "username":"abolfazlansari@aut.ac.ir",
    "password":"Icannontsharemypass",
        }'''

# def is_student(username, password): -> it breaks to get_password
    # check this username is valid or not
    # check the correction of password
    # zahra side
    # database side
    # return 1,0 
    # pass

# We do not have MH login at this point



# The process of checking username and password
# get Pass from database


def login(username: 'str', password: 'str'):

    database_password = get_password(username)

    if database_passowrd == password:
        return 'is_successful'
    else:
        return 'error_string'

