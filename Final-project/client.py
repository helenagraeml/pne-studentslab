import http.client
import json

SERVER = "localhost"
PORT = 8080


def make_request(name, path, params=""):
    print(f"--- {name} ---")
    if params:
        full_path = f"{path}?{params}&json=1"
    else:
        full_path = f"{path}?json=1"

    conn = http.client.HTTPConnection(SERVER, PORT)

    try:
        conn.request("GET", full_path)
        res = conn.getresponse()
        print(f"Response {name}: {res.status} {res.reason}")
        data = res.read().decode("utf-8")
        result = json.loads(data)
        if path == "/":
            print(result["message"])

        elif path == "/listSpecies":
            species = result["species"]
            print(f"limit selected: {result["limit"]}")
            for i in species:
                print(f"-{i}")

        elif path == "/karyotype":
            karyotype = result["karyotype"]
            print(f"Karyotype for {result['species']}:")
            for i in karyotype:
                print(f"-{i}")

        elif path == "/chromosomeLength":
            print(f"Chromosome length: {result['length']}")

        elif path == "/geneLookup":
            print(f"ID for gene {result['gene']}: {result['id']}")

        elif path == "/geneSeq":
            print(f"Sequence: {result['seq']}")

        elif path == "/geneInfo":
            print(f"Gene Info: \n Start : {result['start']} \n End : {result['end']} \n Length: {result['length']}")

        elif path == "/geneCalc":
            percentage = result['percentage']
            print(f"Gene calculations : \n Length: {result['length']}")
            for i in percentage:
                print(f"{i} : {percentage[i]}")

        elif path == "/geneList":
            overlap = result['genes']
            print(f"Names of the human genes that overlap the region:")
            for i in overlap:
                print(f"-{i}")

        else:
            print(data)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    print("-" * 30 + "\n")


make_request("Index", "/")
# 1) listSpecies
make_request("List Species", "/listSpecies", "limit=10")

# 2) karyotype
make_request("Karyotype", "/karyotype", "species=human")

# 3) chromosomeLength
make_request("Chromosome Length", "/chromosomeLength", "species=human&chromo=X")

# 4) geneLookup
make_request("Gene Lookup", "/geneLookup", "gene=FRAT1")

# 5) geneSeq
make_request("Gene Sequence", "/geneSeq", "gene=FRAT1")

# 6) geneInfo
make_request("Gene Info", "/geneInfo", "gene=FRAT1")

# 7) geneCalc
make_request("Gene Calculation", "/geneCalc", "gene=FRAT1")

# 8) geneList
make_request("Gene List", "/geneList", "chromo=9&start=22125500&end=22136000")