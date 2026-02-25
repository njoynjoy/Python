import requests
from requests.auth import HTTPBasicAuth
import json

url = "<your url>.net/rest/api/3/issue"

#api token
auth = HTTPBasicAuth("gmail", API_token)
headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
payload = json.dumps( {
  "fields": {
    "project": {
      "key": "NJOYN"
    },
    "issuetype": {
      "id": "10008"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

print (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
