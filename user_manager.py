from create_user import User

class UserManager(User):
        def __init__(self):
              self.user = {}

        # check if new or old user
        def check_user_status(self):
              status = input("Are you a new user?(yes/no): ")
              if status == "yes":
                     user = User.create_user()
                     self.user[user.name] = user
                     return user