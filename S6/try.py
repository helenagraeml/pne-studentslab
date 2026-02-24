class Seq: #class Animal, class person....
    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def lenth(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


class Gene(Seq):


    def __init__(self, strbases, name=""):
        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases



# Main program
# Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRATI1")
print("Testing...")

# -- Printing the objects
# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.lenth()}") #s1.name_of_the_fuction()
print(f"Sequence 2: {g}")
print(f"  Length: {g.lenth()}")



class ClassName:
    #Constructor (_int_) method to iniziate attributes.
    def __init__(self, attribute1, attribute2): #paramitar self is always magnatory, then you can add as many parameters as you want
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        #method to define actions or behavours
    def method_name(self, parameter):
        #perform  opertations on attributes on other task
         pass

