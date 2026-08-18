class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 10
        self.following = 100
    def follow(self):
        self.following+=1
        sef.followers+=1
user_1 = User(1,"HP")
user_2 = User(2,"HP")
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
