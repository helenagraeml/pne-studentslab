from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    s= "S04/sequences/"
    files = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt" ]
    dic = {}
    for f in files:
        content =  Path(s+f).read_text()
        base = { "A": 0 ,"C": 0 , "G": 0 , "T":0 }
        f = f.split(".")
        f = f[0]
        dic[f] = seq_count_base(content, base)

    print("-----| Exercise 4 |------")
    for key, value in dic.items():
        print(f"Gene : {key}")
        for k, v in value.items():
            print(f"   {k} : {v}")