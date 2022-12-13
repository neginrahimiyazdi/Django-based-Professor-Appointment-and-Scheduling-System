import json

def show_mh_day_meetings(mh_id, date): 
    pass #zahra side
    
def mh_get_time_table(input):
  
    input = json.loads(input)
    mh_id, date = input['mh_id'], input['date']
    mh_meetings =  show_mh_day_meetings(mh_id['mh_id'],date['date'])
    #meetings[0] = start_time
    #meetings[1] = end_time
    meeting_list = []

    for meeting in mh_meetings:
        
        start_time = meeting[0]
        end_time = meeting[1]      
        meeting_list.append({"start_time": start_time, "Score": end_time})         

    return json.dumps(meeting_list)

  
input = '''{ 
    "mh_id":"123", 
    "start_day":[{"date":"12/08/2022", "meetings":[{"start_time":"12:30", "end_time"="13:30"}, {"start_time":"17:30", "end_time"="18:30"}]}
          ]}
        '''