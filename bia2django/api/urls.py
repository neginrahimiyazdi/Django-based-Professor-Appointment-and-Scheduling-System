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
    path('get_timetaible/', views.api_get_timetaible),
    path('mh_timeline/', views.api_mh_timeline)
    
}