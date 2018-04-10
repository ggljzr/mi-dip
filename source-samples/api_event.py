import requests

# stejné jako při zasílání kontrolního hlášení
# liší se pouze url
url = 'https://raspberrypi.local/api/smoke_event'
headers = {'apikey' : api_key}

r = requests.post(url, headers=headers, verify=False)

if r.status == 201:
    # odpověď neobsahuje žádná data
    ...
