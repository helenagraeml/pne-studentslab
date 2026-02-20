from pathlib import Path
from Seq0 import *
if __name__ == "__main__":
    s = "S04/sequences/"
    files = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
    dic = {}
    for f in files:
        content = Path(s + f).read_text()
        f = f.split(".")
        f = f[0]
        dic[f] = seq_len(content)
    print("-----| Exercise 3 |------")
    for k, v in dic.items():
        print(f"Gene {k} ----> Length : {v}")



