from django.urls import path
from . import views

# URLConf
urlpatterns = {
    path('register_user/', views.api_register_user), 
    path('register_mh/', views.api_register_mh), 
    path('login/', views.api_login), 
    path('mh_fill_timetable/', views.api_mh_fill_timetable),
    path('get_list_of_mh/', views.api_get_list_of_mh),
    path('reserve_meeting/', views.api_reserve_meeting),
    path('get_timetable/', views.api_get_timetable),
    path('get_mh_timeline/', views.api_get_mh_timeline),
    path('get_user_timeline/', views.api_get_user_timeline),
    path('get_mh_account/', views.api_get_mh_account),
    path('get_user_account/', views.api_get_user_account),
    path('fill_mh_account/', views.api_fill_mh_account),
    path('fill_user_account/', views.api_fill_user_account),
    

}