class user:
    def user(self,username,password,ID):
        self.username=username
        self.password=password
        self.ID=ID

user_1 = user()
user_1.username="Username_1"
user_1.password="1234"
user_1.ID="1234"
print(user_1.username)

class company:
    def __init__(self, name):
        self.name=name

Userdetails = company("HP")
print(Userdetails.name)
