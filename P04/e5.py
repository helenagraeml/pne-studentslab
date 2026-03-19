from pathlib import Path
import socket
if __name__ == "__main__":
    IP = "127.0.0.1"
    PORT = 8080


    def process_client(s):
        req_raw = s.recv(2000)
        req = req_raw.decode()

        if not req:
            return

        lines = req.split('\n')
        req_line = lines[0]
        parts = req_line.split(" ")

        if len(parts) < 2:
            return

        path = parts[1]
        print("Request line:", req_line)
        if path == "/info/A":
            FILENAME = "../P04/html/info/A.html"


        elif path == "/info/C":
            FILENAME = "../P04/html/info/C.html"

        elif path == "/info/G":
            FILENAME = "../P04/html/info/G.html"

        elif path == "/info/T":
            FILENAME = "../P04/html/info/T.html"

        else:
            FILENAME = "../P04/html/info/error.html"


        body = Path(FILENAME).read_text()
        status_line = "HTTP/1.1 200 OK\r\n"


        header = "Content-Type: text/html\r\n"
        header += f"Content-Length: {len(body)}\r\n"

        response_msg = status_line + header + "\r\n" + body
        s.send(response_msg.encode())


    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ls.bind((IP, PORT))
    ls.listen()


    while True:
        print("Waiting for clients....")
        try:
            (cs, client_ip_port) = ls.accept()
            process_client(cs)
            cs.close()
        except KeyboardInterrupt:
            print("Server stopped!")
            ls.close()
            exit()
