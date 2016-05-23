# !/usr/bin/python

__AUTHOR__='Abhijeet Mohan'

from gcm import GCM
import requests
import ConfigParser
from pprint import pprint

# Read config
config = ConfigParser.RawConfigParser()
config.read('constants.cfg')

# Constant doc url
DOC_URL = config.get('doc')

# updating api key
API_KEY = config.get('API_KEY')

# bulding GCM object from API_KEY
gcm = GCM(API_KEY)

# downloading document from url
r = requests.get(DOC_URL)
data = r.text
rows = data.split('\n')

# Plaintext request
reg_id = config.get('REG_ID')
for row in rows:
    # making gcm request
    gcm.plaintext_request(registration_id=reg_id, data=row)

# Extra arguments
res = gcm.json_request(
    registration_ids=reg_ids, data=data,
    collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
)

# output response
pprint(res)
