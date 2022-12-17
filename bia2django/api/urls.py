from django.urls import path
from . import views

# URLConf
urlpatterns = {
    path('register_user/', views.api_register_user), 
    path('register_mh/', views.api_register_mh), 
    path('login/', views.api_login), 
    path('mh_fill_timetable/', views.api_mh_fill_timetable)
}