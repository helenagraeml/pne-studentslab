import socket
from Seq1 import Seq
# echo "GET 1" | nc 127.0.0.1 8080
# echo "GET 2" | nc 127.0.0.1 8080
# echo "GET 3" | nc 127.0.0.1 8080
# echo "GET 4" | nc 127.0.0.1 8080
# echo "PING" | nc 127.0.0.1 8080
# echo "INFO AACCGTA" | nc 127.0.0.1 8080

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server configured!")
lst = ["ACGTG", "TGTGCC", "ACTGC", "ACCG"]
while True:
    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().strip().split(" ")
        command = msg[0]

        if command == "PING":
            print(f"{command} connected!")
            response = "OK!" + "\n"
            cs.send(response.encode())
            cs.close()

        elif command == "GET":
            num = msg[1]
            n = int(num)
            if 0<= n <= 4:
                print(f"{command}")
                response = lst[n] + "\n"
                print(lst[n])
                cs.send(response.encode())
                cs.close()

            else:
                print(f"{msg}")
                response = "NOT AN OPTION"

                cs.send(response.encode())
                cs.close()
        elif command == "INFO":
            seq = msg[1].strip()
            total = len(seq)

            a = seq.count("A")
            c = seq.count("C")
            g = seq.count("G")
            t = seq.count("T")

            print(f"{command}")
            print("New sequence created!")

            l= f"sequence {seq}" + f"Total length: {total}\n" + f"A: {a} ({a / total * 100:.1f}%)\n" + f"C: {c} ({c / total * 100:.1f}%)\n" + f"G: {g} ({g / total * 100:.1f}%)\n" + f"T: {t} ({t / total * 100:.1f}%)\n"
            print(l)
            response =l

            cs.send(response.encode())
            cs.close()

