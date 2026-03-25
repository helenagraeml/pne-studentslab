import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8080
IP = "127.0.0.1"
s.connect((IP, PORT))
flag = True
while True:
    msg = input("Enter a number:")
    s.send(str.encode(msg))
    response = s.recv(2048).decode("utf-8")
    if response != "lower" or response != "higher":
        flag = False
        print(f"{response}")
        s.close()
    else:
        print(f"{response}")
