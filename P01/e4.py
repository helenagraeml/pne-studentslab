from Seq1 import Seq

if __name__ == "__main__":
    print("-----| Practice 1, Exercise 4|------")
    s1 = Seq()
    s2 = Seq("TATAC")
    s3 = Seq("Invalid sequence")
    print(f"Sequence 1 : (Length: {s1.length()}) {s1}")
    print(f"Sequence 2 : (Length: {s2.length()}) {s2}")
    print(f"Sequence 3 : (Length: {s3.length()}) {s3}")