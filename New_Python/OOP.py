class Dog: 

    attrib1 = "mammal"

    def __init__(self,name):
        self.name = name

    def speak(self):
            print("My name is {}".format(self.name))

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attrib1))
print("Tommy is a {}".format(Rodger.__class__.attrib1))

print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

Tommy.speak()
Rodger.speak()