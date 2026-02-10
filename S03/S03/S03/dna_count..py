seq = input("Enter the sequence: ")
seq = seq.upper()
print("Total lenth : ", len(seq))

bases =  {"A": 0 , "C": 0, "G": 0, "T": 0}

for base in seq:
    if base in bases:
        bases[base] += 1

for base, count in bases.items():
    print(f"{base}: {count}")
