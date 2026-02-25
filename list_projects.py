# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "<your url>.net/rest/api/3/project"

# API_token
auth = HTTPBasicAuth("13cn240@gmail.com", API_token)
headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)
for project in output:
    print(project['key'], project['name'])
