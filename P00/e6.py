from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    SEQUENCE = "S04/sequences/"
    FILENAME = "U5.txt"
    filename = Path(SEQUENCE + FILENAME).read_text()
    f = FILENAME.split(".")
    f = f[0]
    F = seq_read_fasta(filename)
    R = seq_reverse(F, 20)

    print("------| Exercise 6 |------")
    print("Gene ", f)
    print("Fragment: ",F)
    print("Reverse:  ", R)

