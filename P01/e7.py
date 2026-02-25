from Seq1 import Seq

if __name__ == "__main__":
    print("-----| Practice 1, Exercise 6|------")
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    lst = [s1, s2, s3]
    n = 1
    for i in lst:
        print(f"Sequence {n} : (Length: {i.length()}) {i} ")
        print(f"{i.count()}")
        print(f"REV: {i.reverse()}")
        n += 1