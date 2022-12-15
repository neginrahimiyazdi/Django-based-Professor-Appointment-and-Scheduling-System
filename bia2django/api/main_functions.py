from .ORM.functions import remove_mh_day_meetings, append_time, append_mh_time
import json

input = '''{ 
    "mh_id":"123", 
    "days":[{"date":"12/08/2022", "meetings":[{"start_time":"12:30", "end_time"="13:30"}, {"start_time":"17:30", "end_time"="18:30"}]}
           ,{"date":"12/09/2022", "meetings":[{"start_time":"14:30", "end_time"="15:30"}]}
          ]}
        '''

def mh_fill_timetable(input):
    try:
        mh_id, days = input['mh_id'], input['days']
        for day in days:
            remove_mh_day_meetings(mh_id, day['date']) 
            for mh_time in day['meetings']:
                time_id = append_time(day['date'], mh_time['start_time'], mh_time['end_time'])
                append_mh_time(mh_id, time_id)

        output = {
        "is_succesfull": True,
        "error_string": "",
        }

    except Exception as e:
        output = {
        "is_succesfull": False,
        "error_string": str(e),
        }
        
    return output