# Class: class is a blueprint or template, it defined  object Eg: examination form
# Object : Specific instance created from the template eg: from which contains the  data of john

class employee:
      company = "My Company" # Class attribute
      def get_salary(self): # self is very important self is a only way to reference the object of class which is being created
          return 20000
      def __init__(self,Bondperiod,readytojion,noticeperiod,company): #__init__() is not treated like an ordinary method. It is a special method that Python automatically runs when the object is created.
          self.Bondperiod=Bondperiod
          self.readytojion=readytojion
          self.noticeperiod=noticeperiod
          self.company=company
      def get_np(self):
          return self.Bondperiod
#Object Introspection
print(dir(employee))

Emp6 = employee("4years","yes","1month","Instance attribute :Complanyname") # here company is instance attribute
print(Emp6.company)
Emp3 = employee("2years","Yes","3months","AAA")
print(Emp3.Bondperiod)
print(Emp3.readytojion)
print(Emp3.noticeperiod)
Emp4=employee("3","Yes","2","BBB")
print(Emp4.get_salary())
e=employee("4","No","1","CCC") # an object of class employee is created
print(e.get_salary())
E2=employee("1","Yes","2","EEE")
print(E2.get_salary())
Emp5 = employee("5","Yes","3","FFF")
print(Emp5.get_np())



class person:
    def __init__(self,name,age): #__init__ already configured.The object is created already filled with data.
        self.name=name
        self.age=age
p= person("James",18)
print(p.name)
print(p.age)

class person:
    def personinfo(self,name,age):
        self.name=name
        self.age=age
p= person()
P1 = person()
p.personinfo("James",18)
P1.personinfo("John",20)
print(p.name)
print(p.age)
print(P1.name)