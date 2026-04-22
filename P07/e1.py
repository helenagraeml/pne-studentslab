import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMETER = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETER

print()
print(f"Server : {SERVER}")
print(f"URL : {URL}")
conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMETER)

response = conn.getresponse()
print(response.status, response.reason)
data = json.loads(response.read().decode())
if data["ping"] == 1:
    print("ALIVE!")

