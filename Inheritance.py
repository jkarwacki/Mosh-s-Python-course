class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark!")


class Cat(Mammal):
    # if the class is empty
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()
