import sys,os
from create_user import User
from calorie_calculator import CALculator
from user_manager import UserManager


def _(): # need pytest
    pass

def _(): # need pytest
    pass

def choose_function(calculator): # need pytest
    functions = {"1": "calculator.bmr",
                 "2": "calculator.maintenace_tdee", 
                 "3": "calculator.weightloss_tdee",
                 "4": "calculator.weightgain_tdee"}
    print("1. get bmr")
    print("2. get maintenance TDEE")
    print("3. get weight loss TDEE")
    print("4. get weight gain TDEE")
    user_input = input("Please select menu: ")
    return functions[user_input]()

def main(): # need pytest
    user = User.create_user()
    calculator = CALculator(user)
    print(choose_function(calculator))

if __name__ == "__main__":
      with open("user_db.csv","a") as file:
          file.write(f"testid,12234")
    