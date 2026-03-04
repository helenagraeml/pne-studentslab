from Client0 import Client
from Seq1 import Seq
if __name__ == "__main__":

    PRACTICE = 2
    EXERCISE = 5

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "212.128.255.78"
    port = 8080

    c = Client(ip, port)
    print("Sending a message to the server...")
    head = "../P00/S04/sequences/"
    gene = ["FRAT1"]
    tail = ".txt"

    for i in gene:
        s = Seq()
        s.read_fasta(head + i + tail)
        frag = 0
        lst = []
        sequence = str(s)
        print(f"Gene FRAT1: {sequence}")
        for i in range(5):
            fragment = sequence[i * 10:(i + 1) * 10]
            print(f"Fragment {i + 1}: {fragment}")
            c.talk(fragment)


