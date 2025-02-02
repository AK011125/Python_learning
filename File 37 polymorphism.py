class Animal:
    def speaks(self):
        pass
    
class Dog(Animal):
    def speaks(self):
        print("Barks")

class cat(Animal):
    def speaks(self):
        print("Meow")

class cow(Animal):
    def speaks(self):
        print("Moo")

dog = Dog()
cat = cat()
cow = cow()

dog.speaks()
cat.speaks()
cow.speaks()
