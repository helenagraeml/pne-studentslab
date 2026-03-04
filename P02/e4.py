from Client0 import Client
from Seq1 import Seq
if __name__ == "__main__":

    PRACTICE = 2
    EXERCISE = 4

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "212.128.255.78"
    port = 8080

    c = Client(ip, port)
    print("Sending a message to the server...")
    head = "../P00/S04/sequences/"
    gene = ["U5", "ADA", "FRAT1"]
    tail = ".txt"

    for i in gene:
        s = Seq()
        s.read_fasta(head + i + tail)

        # 1️⃣ Send info message
        print(f"\nTo Server: Sending the {i} Gene to the server...")
        response = c.talk(f"Sending the {i} Gene to the server...")
        print(f"From Server:\n{response}")

        # 2️⃣ Send actual sequence
        print("To Server:", str(s))
        response = c.talk(str(s))
        print(f"From Server:\n{response}")