class parent():
    def __init__ (self):
        self.super_attribute = True
        print("This is a prent class")

class child(parent):
    def __init__(self):
        super().__init__()
        print("This is a child class")
        print(self.super_attribute)

child1 = child()