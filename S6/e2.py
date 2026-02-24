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
    def lenth(self):
        return len(self.bases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

def print_seqs(seq_list):
    position = 0
    for i in seq_list:
        print(f"sequence {position}: (Length: {i.lenth()}) {i}")
        position +=1

