import requests
import json

def fetch_a_joke():
    LINK = "http://icanhazdadjoke.com"
    parameti = {"Accept": "application/json"}

    response = requests.get(LINK, headers = parameti)
    # print(response.content, type(response.content))
    # print(response.text, type(response.text))

    json_response = json.loads(response.text)
    # print(json_response, type(json_response))

    # print(f"Gluma este: {json_response["joke"]}")
    return json_response["joke"]

print(fetch_a_joke())