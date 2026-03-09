from Client0 import Client
from Seq1 import Seq

if __name__ == "__main__":
    PRACTICE = 2
    EXERCISE = 6
    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "127.0.0.1"
    port1 = 8080  # Server 1
    port2 = 8081  # Server 2

    client1 = Client(ip, port1)
    client2 = Client(ip, port2)
    print(client1)
    print(client2)

    head = "../P00/S04/sequences/"
    tail = ".txt"

    s = Seq()
    s.read_fasta(head + "FRAT1" + tail)
    sequence = str(s)

    print(f"Gene FRAT1: {sequence}")

    for i in range(10):
        fragment = sequence[i * 10: (i+1)*10]
        message = f"Fragment {i + 1} : {fragment}"
        print(message)

        if (i + 1) % 2 == 1 :
            client1.talk(message)
        else:
            client2.talk(message)
