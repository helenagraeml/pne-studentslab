class Seq:
    def __init__(self, bases):
        valid_base = ["A", "G", "T", "C"]
        total = 0
        for i in bases:
            if i in valid_base:
                total += 1
        if total == len(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("ERROR!")

    def __str__(self):
        return self.bases

    def  lenth(self):
        return len(self.bases)

def generate_seqs(pattern, number):
    lst = []
    for i in range(1, number + 1):
        new_seq = Seq(pattern * i)
        lst.append(new_seq)
    return lst
def print_seqs(seq_list):
    position = 0
    for i in seq_list:
        print(f"sequence {position}: (Length: {i.lenth()}) {i}")
        position += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
