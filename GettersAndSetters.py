#from OOPs import employee
class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

    @property
    def firstname(self):
        firstname = self.name.split()[0]
        lastname = self.name.split()[-1]
        return firstname,lastname
    @firstname.setter
    def firstname(self,newfirstname):
        lastname = self.name.split()[-1]
        new_name = f"{newfirstname},{lastname}"
        self.name = new_name
        return new_name
        #print(firstname)
    @property
    def set_salary(self):
        return int(self.salary)

    @ set_salary.setter
    def set_salary(self,newsalry):
        if int(self.salary) < 0:
            newsalry = self.salary
            return newsalry
        else:
            print("Salary cannot be less than 0")
            self.salary = newsalry
            newsalry = f"{newsalry}"
            return newsalry


e=Employee("John doe","0")
#e.projects = 10
#print(e.projects)
print(e.firstname)
e.firstname = "Jack"
print(e.firstname)
e.set_salary = "1000"
print(e.set_salary)