from pathlib import Path

FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

f = file_contents.split("\n")
clean_f = f[1:]
print("Body of the U5.txt file:")
for i in clean_f:
    print(f"{i}")