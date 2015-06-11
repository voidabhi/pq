# /usr/bin/py

__author__='Abhijeet Mohan'

from gcm import GCM
import requests

DOC_URL = ''

# updating api key
API_KEY = ''

# bulding GCM object from API_KEY
gcm = GCM(API_KEY)
data = {'param1': 'value1', 'param2': 'value2'}

# downloading document from url
r = requests.get(DOC_URL)
data = r.text

# Plaintext request
reg_id = '12'
gcm.plaintext_request(registration_id=reg_id, data=data)

# JSON request
reg_ids = ['12', '34', '69']
response = gcm.json_request(registration_ids=reg_ids, data=data)

# Extra arguments
res = gcm.json_request(
    registration_ids=reg_ids, data=data,
    collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
)
