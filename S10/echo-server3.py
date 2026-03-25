import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"

connections = 0
clients = []

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while connections < 5:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        connections += 1
        clients.append(client_ip_port)

        print("A client has connected to the server!")
        print(f"CONNECTION {connections}. Client IP: {client_ip_port[0]}; PORT: {client_ip_port[1]}")

        msg = cs.recv(1024).decode()
        termcolor.cprint(f"Message received: {msg}", "green")

        response = "ECHO: " + msg + "\n"
        cs.send(response.encode())

        cs.close()


print("\nList of connected clients:")
for i, client in enumerate(clients, start=1):
    print(f"Client {i}: IP={client[0]}, PORT={client[1]}")

ls.close()