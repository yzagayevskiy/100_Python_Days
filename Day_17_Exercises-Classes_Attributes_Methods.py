class User1:
    def __init__(self):
        print("A new user has been created.")


user_1 = User1()
user_1.id = "001"
user_1.username = "Yevgeniy"

print(user_1.username)


class User2:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_2 = User2("002", "Anna")
print(user_2.username)
print(user_2.followers)

user_3 = User2("003", "Bob")
print(user_3.username)
print(user_3.followers)

user_2.follow(user_3)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)
