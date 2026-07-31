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
        
        def store_user(self,email,user):
              if not os.path.exists("users.json"):
                     with open("users.json", "w") as file:
                            json.dump({"users":[]}, file)

              new_user = {"email": email,"user_info":user}

              with open("users.json","r+", encoding="utf-8") as file:
                     data = json.load(file)
                     data["users"].append(new_user)
                     file.seek(0)
                     json.dump(data, file, indent=2, ensure_ascii=False)
      
        def search_user_database(self,email):
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
              with open("users.json","r", encoding="utf-8") as file:
                     loaded_data = json.load(file)
                     for user in loaded_data["users"]:
                            if user["email"] == email:
                                   return user["user_info"]