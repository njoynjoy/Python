from flask import Flask # Import the Flask class from the flask module
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__) # Creating a falsk application instance with the name of the module

@app.route("/createJIRA", methods=["POST"]) #  decorater before executing of the function Define a route for the root URL ("/") and associate it with the hello_world function

def createJIRA(): # Define a function that will be called when the root URL is accessed
    url = "<your url>.net/rest/api/3/issue"

   # API_token

    auth = HTTPBasicAuth("13cn240@gmail.com", API_token)
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

app.run(host='0.0.0.0', port=5000) # Run the Flask application, which will start a local development server and listen for incoming requests
