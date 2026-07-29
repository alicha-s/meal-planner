from create_user import User
import csv,re,json,os
from pathlib import Path

class UserManager():
        # check if new or old user

        def check_valid_email(self,email):
               pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
               result = re.match(pattern, email)
               if result is None:
                      raise EOFError("invalid email")

        #def check_user_status(self):
              #status = input("Are you a new user?(yes/no): ")
              #return status
        
        def store_user(self,email,user):
               data = {"users":[{"email": email,"user_info":user}]}
               with open("users.json","a", encoding="utf-8") as file:
                      json.dump(data, file, indent=2, ensure_ascii=False)
      
        def search_user_database(self,email):
               if not os.path.exists("users.json"):
                     with open("users.json", "w") as file:
                            json.dump({}, file)

               with open("users.json","r", encoding="utf-8") as file:
                     loaded_data = json.load(file)
                     if "users" in loaded_data:
                            for user in loaded_data["users"]:
                                   if user["email"] == email:
                                          return True
                                   else:
                                          return False
                     else:
                            return False

              
        def get_user_info(self,email):
               with open("users.json") as file:
                      for row in file:
                             column = row.rstrip().split("|") 
                             if column[0] == email and column[1] != "":
                                    return column[1]
              