from pathlib import Path
class Seq:
    def __init__(self, bases=None):
        valid_base = ["A", "G", "T", "C"]
        total = 0

        if bases is None:
            self.bases = "NULL"
            print("NULL sequence created!")
        else:
            for i in bases:
                if i in valid_base:
                    total += 1
            if total == len(bases):
                self.bases = bases
                print("New sequence created!")

            else:
                self.bases = "ERROR"
                print("INVALID sequence!")

    def __str__(self):
        return self.bases

    def  length(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            count = 0
            for i in self.bases:
                if i == base:
                   count += 1
            return count

    def count(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return { "A": 0 , "C":0 , "T":0 , "G":0}
        else:
            dic = { "A": 0 , "C":0 , "T":0 , "G":0}
            for i in self.bases:
                if i == "A":
                    dic["A"] += 1
                elif i == "C":
                    dic["C"] += 1
                elif i == "T":
                    dic["T"] += 1
                else:
                    dic["G"] += 1
            return dic
    def reverse(self):
        if self.bases == "ERROR":
            return "ERROR"
        elif self.bases == "NULL":
            return "NULL"
        else:
            return self.bases[::-1]

    def complement(self):
        if self.bases == "ERROR":
            return "ERROR"
        elif self.bases == "NULL":
            return "NULL"
        else:
            lst = []
            for i in self.bases:
                if i == "A":
                    lst.append("T")
                elif i == "T":
                    lst.append("A")
                elif i == "C":
                    lst.append("G")
                else:
                    lst.append("C")
            return "".join(lst)

    def read_fasta(self, filename):
        valid_base = {"A", "G", "T", "C"}

        seq = Path(filename).read_text()
        seq = seq.split("\n")
        clean_seq = "".join(seq[1:]).strip()
        valid = True

        for base in clean_seq:
            if base not in valid_base:
                valid = False
                break

        if valid:
            self.bases = clean_seq
        else:
            self.bases = "ERROR"

        return self.bases

    def most_frequent_seq(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return None

        counts = self.count()
        max_base = None
        max_value = -1

        for base in counts:
            if counts[base] > max_value:
                max_value = counts[base]
                max_base = base

        return max_base



