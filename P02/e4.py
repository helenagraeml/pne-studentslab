from Client0 import Client
from Seq1 import Seq

if __name__ == "__main__":
    PRACTICE = 2
    EXERCISE = 4

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "127.0.0.1"   #"212.128.255.78" (esta es la ip del ordenador que usé)
    port = 8080

    c = Client(ip, port)
    print(c)
    head = "../P00/S04/sequences/"
    gene = ["U5", "ADA", "FRAT1"]
    tail = ".txt"

    for i in gene:
        s = Seq()
        s.read_fasta(head + i + tail)

        print(f"Sending the {i} Gene to the server...")
        response = c.talk(str(s))
        print("From server:")
        print(response)
