import http.server
import socketserver
import os

PORT = 8080


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Define the paths for our HTML files
        # Make sure index.html and error.html are in the same folder as this script
        index_file = 'index.html'
        error_file = 'error.html'

        # Case 1: Main page requested via "/" or "/index.html"
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open(index_file, 'rb') as f:
                self.wfile.write(f.read())

        # Case 2: Any other resource requested
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Serve the error.html file
            if os.path.exists(error_file):
                with open(error_file, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")


# Set up and run the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()