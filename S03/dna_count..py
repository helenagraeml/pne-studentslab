
def count_bases(seq):
    bases =  {"A": 0 , "C": 0, "G": 0, "T": 0}
    for base in seq:
        if base in bases:
             bases[base] += 1
    return bases

if __name__ == "__main__": # para que esta parte no se use en el ejercicio tres y solo coja la funcion de arriba que es la que queremos
    #This if is ignore by any other program except when you run this file
    seq = input("Enter the sequence: ")
    seq = seq.upper()
    print("Total length : ", len(seq))

    result = count_bases(seq)

    for base, count in result.items():
        print(f"{base}: {count}")
