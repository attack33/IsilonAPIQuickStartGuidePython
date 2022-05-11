CLUSTERIP = '172.16.10.10'
PORT = 8080
USER = 'root'
PASS = 'a'


import urllib3
import json
import requests

name = 'test'
path = '/ifs/test'

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning)  # Supressesthe self signed cert warning

uri = f"https://{CLUSTERIP}:{PORT}"
papi = f'{uri}/platform'
headers = {'Content-Type': 'application/json'}
data = json.dumps({'username': USER, 'password': PASS, 'services': ['platform']})
session = requests.Session()
response = session.post(
    f"{uri}/session/1/session", data=data, headers=headers, verify=False)
session.headers['referer'] = uri
session.headers['X-CSRF-Token'] = session.cookies.get('isicsrf')
endpoint = '/6/protocols/smb/shares'

data = json.dumps({'name': name, 'path': path})

response = session.post(papi + endpoint, data=data, headers=headers,verify=False)

if response.status_code == 201:
    print('Success!')
