import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
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

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/" or path == "/index":
            contents = Path('html/index.html').read_text()
        elif path == "/listSpecies":
            ENDPOINT = f"/info/"
            PARAMETER = "?content-type=application/json"
            URL = SERVER + ENDPOINT + PARAMETER
            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMETER)
            res = conn.getresponse()
            data = json.loads(res.read().decode("utf-8"))
            species = data["species"]
            name = ""
            if not arguments:
                limit = "None"
                for i in species:
                    names = values["common_name"]
                    name += "<li>" + names.capitalize() + "</li>"
            else:
                limit = int(arguments["limit"][0])
                for i in species[:limit]:
                    names = values["common_name"]
                    name += "<li>" + names.capitalize() + "</li>"




            contents = self.read_html_file("ping.html").render(context={"limit" : limit})
        elif path == "/karyotype":
            contents = self.read_html_file("get.html").render(context={"species" :specie})
        elif path == "/chromosomeLength":
            contents = self.read_html_file("gene.html").render(context={"species": specie,"chromo": chromosome})


        else:

            contents = Path("html/error.html").read_text()
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