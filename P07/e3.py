import http.client
import json
from e2 import genes

SERVER = "rest.ensembl.org"
GEN = genes["MIR633"]
ENDPOINT = "/sequence/id/"+ GEN
PARAMETER = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETER

def gene_data():
    conn = http.client.HTTPSConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMETER)
        res = conn.getresponse()

        print()
        print(f"Server: {SERVER}")
        print(f"URL: {URL}")
        print(f"Response received!: {res.status} {res.reason}")
        print()

        if res.status == 200:
            data = json.loads(res.read().decode("utf-8"))
            print(f"Gene: MIR633")
            print(f"Description: {data.get('desc')}")
            print(f"Sequence: {data.get('seq')}")
        else:
            print("An error ocurred!")

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()

if __name__ == "__main__":
    gene_data()
