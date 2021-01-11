# animalobjects.py
# practice object-oriented programming
# in the context of animals

class Animal():
    # constructor
    def __init__(self):
        self.name = "Unnamed"
        self.legs = 0
        #print("I'm in the constructor")

    # method
    def talk(self):
        if self.name != "Unnamed":
            print(f"Hello my name is, {self.name}!")
        else:
            print("Hello.")
# creating an animal object
some_animal = Animal()
# access properties
print(some_animal.name)
some_animal.name = "Rex"
some_animal.legs = 2
print(some_animal.name)

# Create a new object

some_other_animal = Animal()
#   * name it whatever
some_other_animal.name = "Jeff"
#   * give it 20 legs
some_other_animal.legs = 20
#   * print out the name and legs
print(f"This animal is called {some_other_animal.name}")
print(f"This animal has {some_other_animal.legs} legs")
some_other_animal.talk()

another_animal = Animal()

