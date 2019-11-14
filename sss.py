import requests
url = 'https://api.ap.kaleyra.io/v1/HXAP1649269665IN/messages/'
payload = 'to=+918638692498&sender=CAMPCO&type=OTP&body=Some message send me the screen shot when you recieve the meesage thanks'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'api-key': 'Aee64e53a44e478f3ce9e71395fc5a813'
}
response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False)
print(response.text)