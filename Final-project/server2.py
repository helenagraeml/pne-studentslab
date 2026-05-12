import http.server
import http.client
import socketserver
import termcolor
from Seq1 import *
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

SERVER = "rest.ensembl.org"
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def read_html_file(self, filename):
        contents = Path("html/" + filename).read_text()
        contents = j.Template(contents)
        return contents

    def seq_read_fasta(self, file_contents):
        lines = file_contents.split("\n")
        seq = lines[1:]
        seq = "".join(seq)
        return seq

    def from_gen_to_id(self, gene):
        ENDPOINT = f"/lookup/symbol/human/"
        GEN = gene
        PARAMETER = "?content-type=application/json"
        conn = http.client.HTTPSConnection(SERVER)
        conn.request("GET", ENDPOINT + GEN + PARAMETER)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        id = data["id"]
        return id

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        is_json = arguments.get("json", ["0"])[0] == "1"
        response_data = {}
        contents = ""
        status_code = 200
        try:
            if path == "/" or path == "/index":
                contents = Path('html/index.html').read_text()
            elif path == "/listSpecies":
                ENDPOINT = f"/info/species"
                PARAMETER = "?content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                species = data["species"]
                name = ""
                if not arguments:
                    limit = "Show all "
                    number = 0
                    for i in species:
                        names = i["common_name"]
                        name += "<li>" + names.capitalize() + "</li>"
                        number += 1
                else:
                    limit = int(arguments["limit"][0])
                    number = 0
                    for i in species[:limit]:
                        names = i["common_name"]
                        name += "<li>" + names.capitalize() + "</li>"
                        number += 1

                contents = self.read_html_file("list_species.html").render(context={"limit" : limit, "number": number, "name": name})
            elif path == "/karyotype":
                select_specie = arguments["species"][0].replace(" ", "%20")
                ENDPOINT = f"/info/assembly/"
                SPECIE = select_specie
                PARAMETER = "?content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + SPECIE + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                species = data["karyotype"]
                names =  ""
                for i in species:
                    names += "<li>" + i+ "</li>"
                contents = self.read_html_file("karyotype.html").render(context={"species" : names})

            elif path == "/chromosomeLength":
                select_specie = arguments["species"][0].replace(" ", "%20")
                select_chromo = arguments["chromo"][0]
                ENDPOINT = f"/info/assembly/"
                SPECIE = select_specie
                PARAMETER = "?content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + SPECIE + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                species = data["top_level_region"]
                length = None
                for i in species:
                    if i["name"] == select_chromo:
                        length = i["length"]
                contents = self.read_html_file("chromosome_length.html").render(context={"length": length})
            elif path == "/geneLookup":
                gene = arguments["gene"][0].replace(" ", "%20").upper()
                id = self.from_gen_to_id(gene)
                contents = self.read_html_file("geneLookup.html").render(context={"id": id, "gene": gene})

            elif path == "/geneSeq":
                gene = arguments["gene"][0].replace(" ", "%20").upper()
                id = self.from_gen_to_id(gene)
                ENDPOINT = f"/sequence/id/"
                GENE = id
                PARAMETER = "?content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + GENE + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                seq = data['seq'].strip()
                contents = self.read_html_file("geneseq.html").render(context={"seq": seq, "gene": gene})
            elif path == "/geneInfo":
                gene = arguments["gene"][0].replace(" ", "%20").upper()
                id = self.from_gen_to_id(gene)
                ENDPOINT = f"/lookup/id/"
                SPECIE = id
                PARAMETER = "?content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + SPECIE + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                start = int(data["start"])
                end = int(data["end"])
                length = end - start + 1
                contents = self.read_html_file("geneinfo.html").render(context={"start": start, "end" : end, "length" : length, "gene": gene, "id": id })
            elif path == "/geneCalc":
                gene = arguments["gene"][0].replace(" ", "%20").upper()
                id = self.from_gen_to_id(gene)
                ENDPOINT = f"/sequence/id/"
                GEN = id
                PARAMETER = "?content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + GEN + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                seq = data['seq'].strip()
                seq_obj = Seq(seq)
                length = seq_obj.length()
                percentage = seq_obj.percentage()
                contents = self.read_html_file("geneCalc.html").render(context={"gene": gene, "length": length, "percentage": percentage})

            elif path == "/geneList":
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]
                ENDPOINT = f"/overlap/region/human/"
                C = chromo
                START = start
                END = end
                PARAMETER = "?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + C + ":" + START + "-"+ END + PARAMETER)
                res = conn.getresponse()
                data = json.loads(res.read().decode("utf-8"))
                genes = []
                for i in data:
                    if i.get("external_name"):
                        genes.append(i["external_name"])
                genes = list(set(genes))
                gene_list = ""
                for i in genes:
                    gene_list += "<li>" + i+ "</li>"
                    contents = self.read_html_file("geneList.html").render(context={"gene_list": gene_list})


            else:
                contents = Path("html/error.html").read_text()
        except Exception as e:
            status_code = 500
            response_data = {"error": str(e)}
            contents = "Internal Server Error"
            self.send_response(status_code)

            if is_json:
                self.send_header('Content-Type', 'application/json')
                body = json.dumps(response_data).encode("utf-8")
            else:
                self.send_header('Content-Type', 'text/html')
                body = str.encode(contents)

            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:

        httpd.serve_forever()

    except KeyboardInterrupt:

        print("")

        print("Stopped by the user")

        httpd.server_close()