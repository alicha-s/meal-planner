import sys,os
from create_user import User
from calorie_calculator import CALculator
from user_manager import UserManager

def main():
    user_manager = UserManager()
    user = user_manager.check_user_status()
    calculator = CALculator(user)
    print(calculator.weightloss_tdee())

if __name__ == "__main__":
    main()