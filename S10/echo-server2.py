import socket
import termcolor
#$ echo "Test" | nc 212.128.255.69 8080
#printf "Test1..." | nc 212.128.255.69 8080

PORT = 8080
IP = "212.128.255.69"
connections = 0

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()


    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        connections += 1
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"CONNECTION {connections}. Client IP: {client_ip_port[0]}; PORT: {client_ip_port[1]}")
        termcolor.cprint(f"Message received: {msg}", "green")


        response = "ECHO: " + msg + "\n"
        cs.send(response.encode())

        cs.close()