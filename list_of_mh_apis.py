import json

def show_all_mh_by_name(): 
    pass #zahra side
    
def get_mh_list():

    mh_list = []
    all_mh =  show_all_mh_by_name()


    for mh in all_mh:
        
        name = mh[0]
        email = mh[1]
              
        mh_list.append({"name": name,"email": email})         

    return json.dumps(mh_list)

  