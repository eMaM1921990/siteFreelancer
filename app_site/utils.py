import json
from siteFreelancer import settings

__author__ = 'emam'

def responeJson(status,message):
    data = {}
    data['status'] = status
    data['message'] = message
    json_data = json.dumps(data)
    return json_data