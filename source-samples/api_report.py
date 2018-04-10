import requests
# server nadřazeného systému je přístupný
# na adrese raspberrypi.local
url = 'https://raspberrypi.local/api/report_event'

# API klíč (získaný například reg. požadavkem)
# je zasílán v hlavičce požadavku
headers = {'apikey' : api_key}

# požadavek 'post', bez ověření
# self-signed certifikátu
r = requests.post(url, headers=headers, verify=False)

if r.status == 201:
    # odpověď -- čas do dalšího hlášení
    period = r.json()['period']