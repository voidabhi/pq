# !/usr/bin/python

__AUTHOR__='Abhijeet Mohan'

from gcm import GCM
import requests
import ConfigParser
from pprint import pprint

CONFIG_PATH = 'constants.cfg'

# Read config
def read_config():
    config = ConfigParser.RawConfigParser()
    config.read(CONFIG_PATH)
    return (config.get('doc_url'), config.get('API_KEY'), config.get('REG_ID'))
    
# Read from excel sheet url
def read_from_url(url):
    r = requests.get(url)
    data = r.text
    rows = data.split('\n')
    return rows

def prepare_msg(row):
    return row.strip()
    
def send_pn():
    (DOC_URL, API_KEY, REG_ID) = read_config()
    
    # bulding GCM object from API_KEY
    gcm = GCM(API_KEY)

    # downloading document from url
    rows = read_from_url(DOC_URL)
    
    # Plaintext request
    for row in rows:
        # build message
        row = prepare_msg(row)
        
        # making gcm request
        gcm.plaintext_request(registration_id=REG_ID, data=row)

    # Json request
    return gcm.json_request(
        registration_ids=reg_ids, data=data,
        collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
    )

if __name__ == '__main__':
    res = send_pn()
    # output response
    pprint(res)
