def count(seq):
    print("total lenth of the sequence is : ", len(seq))
    print("Number of adenine bases:" ,seq.count("A"))
    print("Number of guanine bases:" ,seq.count("G"))
    print("Number of citosine bases:" ,seq.count("C"))
    print("Number of timine bases:" ,seq.count("T"))

seq = input('Enter a DNA sequence: ')
seq = seq.upper()
count(seq)
