SENDERID = 'KLRHXA'
APIKEY = 'A6dc1ee4e0637274a88a23ca6f0711fb6'
VERSION = '4'
BASEURL = "https://api.ap.kaleyra.io/v{}/?api_key={}".format(VERSION, APIKEY)

import requests
url = 'https://api.ap.kaleyra.io/v1/HXAP1649269665IN/messages/'
payload = 'to=+919412680960&sender=KLRHXA&type=MKT&body=Welcome'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'api-key': 'A6dc1ee4e0637274a88a23ca6f0711fb6'
}
response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False)
print(response.text)