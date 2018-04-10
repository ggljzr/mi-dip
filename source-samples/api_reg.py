import requests
# server nadřazeného systemu je přístupný
# na adrese raspberrypi.local
url = 'https://raspberrypi.local/api/garages'

# požadavek 'post', bez ověření
# self-signed certifikátu
r = requests.post(url, verify=False)

if r.status == 201:
    api_key = r.json()['api_key']