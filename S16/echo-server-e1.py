import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path

        if path == "/" or path == "/index":
            contents = Path('html/form-e1.html').read_text()
        elif path == "/echo":
            arguments = parse_qs(url_path.query)
            msg = arguments.get("msg", [""])[0]
            contents = f"""
            <html>
            <body>
                <h1>Recieve message:</h1>
                <p>{msg}</p>
                <a href="/">main page</a>
            </body>
            </html>
            """
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
