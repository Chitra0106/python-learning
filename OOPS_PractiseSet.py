#4

#3
class Animal:
    def __init__(self):
        self.name="Animal"
    def sound(self):
        print("Animal is sound")
class print_sound(Animal):
    def sound(self):
        print("bark")

cat = Animal()
cat.sound()
cat=print_sound()
#2
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_name(self):
        print(f"{self.name} {self.age}")
person1=person("Chitra",20)
person2=person("Sridhar",20)
person2.print_name()


#1
class car:
    def __init__(self, model, year,brand):
        self.model=model
        self.year=year
        self.brand=brand
    def drive(self):
        print("Car is moving")

tiago = car("tiago",2016,"BM")
tiago.drive()
