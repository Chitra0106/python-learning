class Employee:
   company = "HP"
   def __init__(self,name,salary):
       self.name = name
       self.salary = salary
   #instance method (default)
   '''instance method operates on a specific object. 
   It’s the most common method type. It takes self as the first parameter,
    which refers to the specific instance of the class. Instance meth'''
   def print_name(self):
       print(f"{self.name} {self.salary}")

   @staticmethod
   def sum(a,b):
       print(a+b)

   @classmethod
   def print_company(cls):
       print(cls.company)
   @classmethod
   def set_company(cls, new_company):
       cls.company = new_company
       print(cls.company)
   @classmethod
   '''a class method is a method that’s bound to the class 
   rather than any individual instance. It operates on the class itself, 
   not specific objects. Typically, you define it using the @classmethod decorator. 
   The first parameter is cls, which refers to the class itself. This allows the method to access or modify class-level attributes that are shared among all instances.'''

   def set_salary(cls, new_salary):
       if new_salary > 1000:
           cls.salary = new_salary
           print(cls.salary)
       else:
           cls.salary = 1000
           print(cls.salary)

#e = Employee("Jack",1000)
#print(e.name)
#print(e.salary)
a= Employee("Jack",900)
print(a.set_salary(12121))
a.sum(5,5)
a.print_company()
a.set_company("UST")