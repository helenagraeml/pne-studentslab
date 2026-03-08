import socket
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    def ping(self):
        print("OK!")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"
    def talk(self,msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # -- Create the socket
        s.connect((self.ip, self.port))   # establish the connection to the Server (IP, PORT)
        s.send(msg.encode())   # Send data.
        response = s.recv(2048).decode("utf-8") # Receive data
        s.close()  # Close the socket
        return response

