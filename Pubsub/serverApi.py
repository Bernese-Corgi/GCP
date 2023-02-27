import json
import requests

def server_api(path: str, method: str, body):
  result = requests.post(
    f"https://ntest.daybabyday.com/v6/out/shopby",
    data=json.dumps({
        "url": f"https://server-api.e-ncp.com{path}",
        "method": method,
        "header": {
            "systemKey": "b1hLbVFoS1lUeUZVS1EwV1loaVZMQT09",
            "mallKey": "M21OMm8zU1JHUEU1NGFqUURvUklGSk1UNVdvOHc0NkI",
            "version": "1.0"
        },
        "body": body
    })
  )
  
  print(result.json())
  
  return result
