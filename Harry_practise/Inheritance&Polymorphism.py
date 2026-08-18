#Inheritance
class Animal: #parent class
    Location = "India"
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def get_sound(self):
        super().speak()
        print(f"{self.sound} is dog sound")

class _name(Animal):
    def get_name(self):
        super().speak()
        #super().get_sound() it will give error because it is not from parent class


cat = Animal("cat","meow")
print(cat.sound)
cat.speak()
dog = Dog("dog","bow")
#print(dog.speak())
dog.get_sound()
print(dog.Location)