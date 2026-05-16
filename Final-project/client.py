import http.client
import json

PORT = 8080
SERVER = 'localhost'
PARAMS = '?json=1'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

try:
    # Conexión con el servidor
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- 1) LIST OF SPECIES --
    conn.request("GET", "/listSpecies" + PARAMS + "&limit=10")
    r1 = conn.getresponse()
    print(f"Response 1 received: {r1.status} {r1.reason}")
    data1 = r1.read().decode("utf-8")

    # -- 2) KARYOTYPE --
    conn.request("GET", "/karyotype" + PARAMS + "&species=shrew-mouse")
    r2 = conn.getresponse()
    print(f"Response 2 received: {r2.status} {r2.reason}")
    data2 = r2.read().decode("utf-8")

    # -- 3) CHROMOSOME LENGTH --
    conn.request("GET", "/chromosomeLength" + PARAMS + "&species=mouse&chrom=18")
    r3 = conn.getresponse()
    print(f"Response 3 received: {r3.status} {r3.reason}")
    data3 = r3.read().decode("utf-8")

    # -- 4) ID OF A HUMAN GENE --
    conn.request("GET", "/geneLookup" + PARAMS + "&gene=FRAT1")
    r4 = conn.getresponse()
    print(f"Response 4 received: {r4.status} {r4.reason}")
    data4 = r4.read().decode("utf-8")

    # -- 5) SEQUENCE OF A HUMAN GENE --
    conn.request("GET", "/geneSeq" + PARAMS + "&gene=FRAT1")
    r5 = conn.getresponse()
    print(f"Response 5 received: {r5.status} {r5.reason}")
    data5 = r5.read().decode("utf-8")

    # -- 6) INFORMATION ABOUT A HUMAN GENE --
    conn.request("GET", "/geneInfo" + PARAMS + "&gene=FRAT1")
    r6 = conn.getresponse()
    print(f"Response 6 received: {r6.status} {r6.reason}")
    data6 = r6.read().decode("utf-8")

    # -- 7) CALCULATIONS ON A HUMAN GENE --
    conn.request("GET", "/geneCalc" + PARAMS + "&gene=FRAT1")
    r7 = conn.getresponse()
    print(f"Response 7 received: {r7.status} {r7.reason}")
    data7 = r7.read().decode("utf-8")

    # -- 8) GENES OVERLAPPING A REGION --
    conn.request("GET", "/geneList" + PARAMS + "&chromo=9&start=22125500&end=22136000")
    r8 = conn.getresponse()
    print(f"Response 8 received: {r8.status} {r8.reason}")
    data8 = r8.read().decode("utf-8")

    conn.close()

except ConnectionRefusedError:
    print("ERROR: Cannot connect to the Server")
    exit()


# 1) List of species
ls = json.loads(data1)
print("\n--- 1) LIST OF SPECIES ---")
print(f"Limit of species: {len(ls['species'])}")
for species in ls['species']:
    print(f"  - {species}")
print(f"Total number of species: {ls['total']}")

# 2) Karyotype
# Nota: Asegúrate de que tu servidor devuelva una lista en la clave 'karyotype'
karyo = json.loads(data2)
print("\n--- 2) KARYOTYPE ---")
print(f"Karyotype of shrew-mouse:")
if "karyotype" in karyo:
    for chrom in karyo['karyotype']:
        print(f"  - {chrom}")

# 3) Chromosome Length
cl = json.loads(data3)
print("\n--- 3) CHROMOSOME LENGTH ---")
print(f"Length of chromosome 18 in mouse: {cl.get('length')}")

# 4) Gene Lookup
gl = json.loads(data4)
print("\n--- 4) ID OF A HUMAN GENE ---")
print(f"ID of gene FRAT1: {gl.get('id')}")

# 5) Gene Sequence
gs = json.loads(data5)
print("\n--- 5) SEQUENCE OF A HUMAN GENE ---")
print(f"Sequence of gene FRAT1: {gs.get('seq')[:50]}...")

# 6) Gene Info
gi = json.loads(data6)
print("\n--- 6) INFORMATION ABOUT A HUMAN GENE ---")
print(f"Information about gene {gi['gene']}:")
print(f"  Start: {gi['start']}")
print(f"  End: {gi['end']}")
print(f"  Length: {gi['length']}")
print(f"  ID: {gi['id']}")
print(f"  Name of the chromosome: {gi['chromo']}")

# 7) Gene Calculations
gc = json.loads(data7)
print("\n--- 7) CALCULATIONS ON A HUMAN GENE ---")
print(f"Calculations on gene {gc['gene']}:")
print(f"  Length: {gc['length']}")
print("  Percentage of each nitrogenous base in the sequence:")
for base, count in gc['counts'].items():
    percentage = (count / gc['length']) * 100
    print(f"    {base}: {count} ({round(percentage, 1)}%)")

# 8) Gene List (Overlapping)
gl_overlap = json.loads(data8)
print("\n--- 8) GENES OVERLAPPING A REGION ---")
print(f"Overlapped genes in the chromosome {gl_overlap['chromo']}:")
genes_found = gl_overlap.get('region', [])
for gene in genes_found:
    print(f"  - {gene}")


