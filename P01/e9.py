from Seq1 import Seq

if __name__ == "__main__":
    print("-----| Practice 1, Exercise 9 |------")

    s = Seq()
    s.read_fasta("../P00/S04/sequences/U5.txt")

    print(f"Sequence : (Length: {s.length()}) {s}")
    print(f"Bases: {s.count()}")
    print(f"Rev:   {s.reverse()}")
    print(f"Comp:  {s.complement()}")