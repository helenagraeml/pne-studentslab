from Client0 import Client
from Seq1 import Seq
if __name__ == "__main__":

    PRACTICE = 2
    EXERCISE = 5
    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "127.0.0.1"
    port = 8080

    c = Client(ip, port)
    print(c)

    head = "../P00/S04/sequences/"
    tail = ".txt"


    s = Seq()
    s.read_fasta(head + "FRAT1" + tail)
    sequence = str(s)
    print(f"Gene FRAT1: {sequence}")

    for i in range(5):
        fragment = sequence[i * 10:(i + 1) * 10]
        print(f"Fragment {i + 1}: {fragment}")
        c.talk(fragment)


