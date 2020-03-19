class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


person1 = Person("Julian")  
person1.talk()
