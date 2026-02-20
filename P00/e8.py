from pathlib import Path
def most_common_base(seq):
    base_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in seq:
        if base in base_count:
            base_count[base] += 1

    most_frequent = max(base_count, key=base_count.get)
    return most_frequent

if __name__ == "__main__":
    s= "S04/sequences/"
    files = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt" ]
    dic = {}
    for f in files:
        seq =  Path(s+f).read_text()
        f = f.split(".")
        f = f[0]
        dic[f] = most_common_base(seq)

    print("-----| Exercise 5 |------")
    for k, v in dic.items():
        print(f"Gene {k}: Most frequent Base: {v}")


