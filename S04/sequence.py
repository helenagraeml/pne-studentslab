from pathlib import Path
def count(f):
    count = 0
    for i in f:
        count+= len(i)
    return count

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

f = file_contents.split("\n")
clean_f = f[1:]


print("total number of bases ", count(clean_f))