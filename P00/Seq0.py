def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    filename = filename.split("\n")
    seq = filename[1:]
    seq = "".join(seq)
    return seq[:20]

def seq_len(seq):
    seq= seq.split("\n")
    seq = seq[1:]
    seq = "".join(seq)
    return len(seq)

def seq_count_base(seq, base):
    seq = seq.split("\n")
    seq = seq[1:]
    seq = "".join(seq)
    for i in seq:
        if i in base:
            base[i] += 1
    return base

def seq_count(seq):
    base = {"A": 0, "C": 0, "G": 0, "T": 0}
    seq = seq.split("\n")
    seq = seq[1:]
    seq = "".join(seq)
    for i in seq:
        if i in base:
            base[i] += 1
    return base
def  seq_reverse(seq, n):
    return seq[:n][::-1]








