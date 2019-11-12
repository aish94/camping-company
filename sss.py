import requests
url = 'https://api.ap.kaleyra.io/v1/HXAP1649269665IN/messages/'
payload = 'to=+919412680960&sender=KLRHXA&type=TXT&body=message'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'api-key': 'Aee64e53a44e478f3ce9e71395fc5a813'
}
response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False)
print(response.text)