import requests

import datetime
from datetime import datetime
from datetime import timedelta

def search_tag(days, tag):

    
    today_date = datetime.today()
    final_date = datetime.today() + timedelta(days=days)
    PARAMS = {
        'previous_day': today_date,
        'the_next_day': final_date,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    response = requests.get('https://api.stackexchange.com/2.2/questions', params=PARAMS)
    resp_data = response.json()
    
    tags_list = []
    for question in resp_data.get('items'):
        tags_list.append(str(question['tags']))
    return tags_list   

print(search_tag(2, 'python'))
