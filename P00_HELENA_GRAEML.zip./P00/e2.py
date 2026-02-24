from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    SEQUENCE = "S04/sequences/"
    FILENAME ="U5.txt"
    filename = Path(SEQUENCE+FILENAME).read_text()
    print(f"DNA file : {FILENAME}")
    print("The first 20 bases are:", seq_read_fasta(filename))
