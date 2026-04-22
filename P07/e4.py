import http.client
import json
from e2 import genes

SERVER = "rest.ensembl.org"
GEN = genes["MIR633"]
ENDPOINT = "/sequence/id/"+ GEN
PARAMETER = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETER

gene = input("Write the gene name:")
SERVER = "rest.ensembl.org"
GEN = genes[gene]
ENDPOINT = "/sequence/id/"+ GEN
PARAMETER = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETER
print()
print(f"Server : {SERVER}")
print(f"URL : {URL}")
conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMETER)

response = conn.getresponse()
print("Response received!", response.status, response.reason)
data = json.loads(response.read().decode())
print(f"Gene : {data.get('id')} ")
print(f"Description: {data.get('desc')}")
print(f"Bases: {data.get('seq')}")
