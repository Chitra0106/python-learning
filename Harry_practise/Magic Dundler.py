class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f'{self.name}, {self.salary}'
    def __repr__(self):
        return f'{self.name},\n  {self.salary}'
    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary
    def __len__(self):
        return len(self.name)
    
e = employee("John", 100000)
print(str(e))
print(repr(e))
print(len(e))
