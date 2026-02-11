#The position (index) of the word "Python" in the stripped string
#(use find())
#The words joined back together separated by " - " (use split()
#and " - ".join())


text = "  Hello, World! Welcome to Python Programming.  "
text = text.strip()
print("Stripped:", text )
splited = text.split(" ")
print("Word count:", len(splited))
print("Title case:", text.title())
print("Starts with Hello:", text.startswith("Hello"))
print("Ends with ing.:", text.endswith("ing."))
print("Python position: ", text.find("Python") )
print("Joined:"," - ".join(splited))

