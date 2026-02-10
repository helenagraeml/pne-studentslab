
def count_bases(seq):
    bases =  {"A": 0 , "C": 0, "G": 0, "T": 0}
    for base in seq:
        if base in bases:
        bases[base] += 1


seq = input("Enter the sequence: ")
seq = seq.upper()
print("Total lenth : ", len(seq))

result = count_bases(seq)

for base, count in bases.items():
    print(f"{base}: {count}")
