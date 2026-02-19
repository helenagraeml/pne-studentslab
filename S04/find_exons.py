from pathlib import Path

def read_cromosome20(f): #CROMOSOMA
    lines = f.split("\n")
    header1 = lines[0] #aqui se encuentran las coordenadas del cromosoma
    seq1 = "".join(line.strip() for line in lines[1:] if line.strip()).upper() #linea continua con las bases nitrogenadas
    return header1, seq1

def read_exons(e):   # expected : [ (exon1, "ACTGACGT"), (....,....) , ...]
    header2 = []
    seq2 = [] #conjunto de secuencias fimnales
    header = None #nombre del exon
    seq_ex = [] # secuencia del exon
    for i in e.splitlines(): #.splitlines ( lo convierte en una lista de lineas)
       line = i.strip()
       if not line : #saltar lineas vacias
            continue
       elif line.startswith(">"):
            if header is not None: #si ya estabamos leyendo un exon lo guardamos antes de empezar uno nuevo
                header2.append(header)
                seq2.append("".join(seq_ex).upper())

            header = line[1:].strip() # empezamos desde 1 para quitar el >
            seq_ex = []
       else:
           seq_ex.append(line)

    if header is not None:
        header2.append(header)
        seq2.append("".join(seq_ex).upper())
    return header2, seq2 #head = lista de la primera linea identificativa de cada exon    seq = sequencia respectiva de cada exon

def max_boundary(header): #header1
    # estructura del gen : >20 dna:chromosome chromosome:GRCh38:20:44584296:44652852:-1
    part = header.split(":")
    start = int(part[-3])
    end = int(part[-2])
    return max(start, end)

def find_exon(seq1, seq2):
    position = seq1.find(seq2)
    return position

def reverse_strand( maxi, index):
    return maxi - index


exon = "sequences/ADA_EXONS.txt"
e= Path(exon).read_text()
file = "sequences/ADA.txt"
f = Path(file).read_text()

header1, seq1 =  read_cromosome20(f)
bound =  max_boundary(header1)
header2, seq2 = read_exons(e)

print( "Exont\tLong\tStart\tEnd")
for i in range(len(seq2)):
    seq = seq2[i]
    start_index = find_exon(seq1, seq)
    length = len(seq)
    end_index = start_index + length -1

    #transformar a la hebra negativa

    cord1 = int(reverse_strand(bound, start_index))
    cord2 = int(reverse_strand(bound, end_index))
    chr_start = min(cord1, cord2)
    chr_end = max(cord1, cord2)
    print(f"{i+1}\t{length}\t{chr_start}\t{chr_end}")




