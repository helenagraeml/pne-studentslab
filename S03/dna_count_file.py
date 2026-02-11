from dna_count import count_bases

if __name__ == "__main__":

# WAY 1
f = open ("dna.txt", "r")
#here we put the code
lines = f.readlines()
f.close() #important to close the terminal


# WAY 2
with open( "dna.txt", "r") as f:
    lines = f.readlines()

total_number = 0
bases =  {"A": 0 , "C": 0, "G": 0, "T": 0}
for seq in lines:
    seq = seq.strip()

    total_number += len(seq)
    for base in seq:
        if base in bases:
            bases[base] += 1

print("Total number of bases: ", total_number)


for base, count in bases.items():
    print(f"{base}: {count}")


