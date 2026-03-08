from Client0 import Client
from Seq1 import Seq
import socket

if __name__ == "__main__":

    ip = "212.128.255.78"
    port1 = 8080  # Server 1
    port2 = 8081  # Server 2

    frat1 = "../P00/S04/sequences/FRAT1.txt"
    with open(frat1, "r") as f:
        lines = f.read().splitlines()

    if lines[0].startswith(">"):
        lines = lines[1:]
    frat1 = "".join(lines)
    lst = []
    for i in range(0, len(frat1), 10):
        fragment = frat1[i:i + 10]
        lst.append(fragment)

    client1 = Client(ip, port1)
    client2 = Client(ip, port2)

    print("-----| Practice 2, Exercise 6 |------")
    print(client1)
    print(client2)
    print("NULL Seq created")
    print(f"Gene FRAT1: {frat1}...")

    # Send fragments to servers
    for idx, fragment in enumerate(lst):
        print(f"Fragment {idx + 1}: {fragment}")
        if (idx + 1) % 2 == 1:  # Odd → server 1
            response = client1.talk(fragment)
        else:  # Even → server 2
            response = client2.talk(fragment)
        # Optional: print server response
        # print("Server response:", response)

