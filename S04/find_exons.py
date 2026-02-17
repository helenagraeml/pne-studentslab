from pathlib import Path

exon = "sequences/ADA_EXONS.txt"
e= Path(exon).read_text()
file = "sequences/ADA.txt"
f = Path(file).read_text()



print(e)
