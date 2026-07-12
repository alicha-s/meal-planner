from create_user import User
import sqlite3

class UserManager():
        def __init__(self):
              self.user_status = self.check_user_status()
              if self.user_status == "yes":
                     self.email = input("Please enter your email: ")
                     self.found_user = self.search_user_database()
                     if self.found_user:
                            print("This email address is already registered.")
                     else:
                            self.user = User.create_user()

        # check if new or old user
        def check_user_status(self):
              status = input("Are you a new user?(yes/no): ")
              return status
        
        def store_user(self):
               with open("user_db.csv") as file:
                      file.write(f"{self.email},{self.user}")
      
        def search_user_database(self):
               with open("user_db.csv") as file:
                      for row in file:
                             column = row.rstrip().split(",") 
                             if column[0] == self.email:
                                    return True
                             else:
                                    return False
              