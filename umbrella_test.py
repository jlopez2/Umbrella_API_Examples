import requests
import json

url = "https://s-platform.api.opendns.com/1.0/events?customerKey=blahblahblah"

payload = {
    "alertTime": "2019-01-24T11:14:26.0Z",
    "deviceId": "12345",
    "deviceVersion": "1a",
    "dstDomain": "internetbadguys.com",
    "dstUrl": "http://internetbadguys.com/a-bad-url",
    "eventTime": "2019-01-24T09:30:26.0Z",
    "protocolVersion": "1.0a",
    "providerName": "James Security Platform"
    }


header = {"Content-type": "application/json"} 

r = requests.post(url, data=json.dumps(payload), headers=header)

print(r.status_code, r.reason)

