class Seq:
    def __init__(self, bases=None):
        valid_base = ["A", "G", "T", "C"]
        total = 0

        if bases is None:
            self.bases = "NULL "
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
        return len(self.bases)

