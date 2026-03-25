import socket
import random
class NumberGuesser:
    def __init__(self, secret_number, attempts):
        self.secret_number = secret_number
        self.attempts = attempts

    def guess(self, number):
        self.attempts.append(number)
        if number == self.secret_number:
            return f"You won after {len(self.attempts)} attempts"
        elif number > self.secret_number:
            return "lower"
        elif number < self.secret_number:
            return "higher"

PORT = 8080
IP = "127.0.0.1"
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((IP, PORT))
ss.listen(1)
print("Waiting for the client to connect")
try:
    (cs, client_ip_port) = ss.accept()
    secret_num = NumberGuesser(random.randint(1, 100))
    flag = True
    while True:
        print("Guess the number:")
        msg = cs.recv(2048)
        if not msg:
            break
        try:
            msg = msg.decode()
            msg = int(msg)
            response = secret_num.guess(msg)
            cs.send(response.encode())
            if response != "lower" or response != "higher":
                cs.close()


except KeyboardInterrupt:
    print("Server stopped by the user")
    ss.close()
    exit()








