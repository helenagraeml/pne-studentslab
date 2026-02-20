from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    SEQUENCE = "S04/sequences/"
    FILENAME = "U5.txt"
    filename = Path(SEQUENCE + FILENAME).read_text()
    f = FILENAME.split(".")
    f = f[0]
    F = seq_read_fasta(filename)
    R = seq_complement(F)
    print("------| Exercise 7 |------")
    print("Gene ", f)
    print("Frag: ", F)
    print("Comp: ", R)