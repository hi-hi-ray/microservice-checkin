import json
import urllib3
from botocore.vendored import requests

def lambda_handler(event, context):
    print(event)
    data = event["Records"][0]["body"]
    message = data

    txt = message.split()
    name = 'Filaignore'

    order = {
        "name": "Filaignore",
        "quantity": int(txt[5])
    }

    jsonData = json.dumps(order)

    print(order)
    url = "http://18.228.238.155/toy/" + txt[3]
    print(url)

    http = urllib3.PoolManager()
    r = http.request('PUT', url,
                     headers={'Content-Type': 'application/json'},
                     body=jsonData)

    return {
        'statusCode': r.status
    }
