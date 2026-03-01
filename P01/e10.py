from Seq1 import Seq

if __name__ == "__main__":
    print("-----| Practice 1, Exercise 10 |------")
    head = "../P00/S04/sequences/"
    gene = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
    tail = ".txt"

    for i in gene:
        s = Seq()
        s.read_fasta(head + i + tail)
        print(f"Gene {i}: Most frequent base: {s.most_frequent_seq()}")