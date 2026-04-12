import http.server
import socketserver
from pathlib import Path

# Definimos el puerto
PORT = 8080


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Determinar qué archivo se solicita
        # Si la ruta es '/', servimos index.html (la página amarilla de tu imagen)
        if self.path == '/':
            file_path = Path("index.html")
        else:
            # Convertimos la URL en una ruta de archivo local (quitando la '/')
            # Ejemplo: '/blue.html' -> 'blue.html'
            file_path = Path(self.path.lstrip('/'))

        try:
            # 2. Intentar leer el archivo solicitado
            # .read_bytes() abre y lee el archivo en formato binario
            content = file_path.read_bytes()

            # Si el archivo existe, enviamos respuesta 200 OK
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            # 3. Si el archivo NO existe, enviamos respuesta 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Intentamos servir tu archivo error.html
            error_file = Path("error.html")
            if error_file.exists():
                self.wfile.write(error_file.read_bytes())
            else:
                # Si ni siquiera existe error.html, enviamos un mensaje básico
                self.wfile.write(b"<h1>404 Not Found</h1><p>Archivo no encontrado.</p>")


# --- Configuración y arranque del servidor ---
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor ejecutándose en: http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
        httpd.server_close()