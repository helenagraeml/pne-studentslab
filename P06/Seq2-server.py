import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

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
        seq = {
            0: "AAGGT",
            1: "ACACT",
            2: "ACGACG",
            3: "ACGTACGT",
            4: "TGCATGCA"}
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/" or path == "/index":
            contents = Path('html/index.html').read_text()
        elif path == "/ping":
            contents = self.read_html_file("ping.html").render(context={})
        elif path == "/get":
            seqnumber = int(arguments["n"][0])
            sequence = seq[seqnumber]
            contents = self.read_html_file("get.html").render(context={"seqnumber" :seqnumber, "sequence": sequence})
        elif path == "/gene":
            gene_name = arguments["name"][0]
            file_path = f"../P00/S04/sequences/{gene_name}.txt"
            raw_file_content = Path(file_path).read_text()
            sequence_data = self.seq_read_fasta(raw_file_content)
            contents = self.read_html_file("gene.html").render(context={
                "name": gene_name,
                "sequence": sequence_data
            })
        elif path == "/operation":
            sequence = arguments.get("seq", [""])[0].upper()
            op = arguments.get("op", ["info"])[0]
            result = ""

            if op == "info":
                length = len(sequence)
                a = sequence.count('A')
                c = sequence.count('C')
                g = sequence.count('G')
                t = sequence.count('T')
                result = (f"Total length: {length}<br>"
                          f"A: {a} ({a * 100 / length}%)<br>"
                          f"C: {c} ({c * 100 / length}%)<br>"
                          f"G: {g} ({g * 100 / length}%)<br>"
                          f"T: {t} ({t * 100 / length}%)")

            elif op == "comp":
                complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
                result = "".join([complement.get(base, base) for base in sequence])

            elif op == "rev":
                result = sequence[::-1]

            contents = self.read_html_file("operation.html").render(context={
                "op": op,
                "sequence": sequence,
                "result": result
            })


        else:
            contents = Path("html/error.html").read_text()


        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return

# ------------------------
# - Server MAIN program
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
