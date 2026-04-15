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

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        seq = {
            0 : "AA",
            1 : "ACAC",
            2 : "ACGACG",
            3 : "ACGTACGT",
            4 : "TGCATGCA"}

        if path == "/" or path == "/index":
            contents = Path('html/index.html').read_text()
        elif path == "/ping":
            contents = self.read_html_file("ping.html").render(context={})
        elif path == "/get":
            seqnumber = arguments["n"][0]
            sequence =  seq[seqnumber]
            contents = self.read_html_file("get.html").render(context={"seqnumber" :seqnumber, "sequence": sequence})

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
