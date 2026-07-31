import sys,os,subprocess,keyboard
from create_user import User
from calorie_calculator import CALculator
from user_manager import UserManager

def get_user_data():
    user_input = {"name":[str,"Name: "],
        "age":[int,"Age: "],
        "weight":[int,"Weight(kg): "],
        "height":[int,"Height(cm): "],
        "sex":[str,"Sex(male/female): "],
        "activity":[int,"Activity(Please input number 1~4\nSedentary= 1/Lightly Active= 2/Moderately Active= 3/Very Active= 4): "],
        "goal":[int,"Goal(Please input number 1~3\nlose weight= 1/maintain= 2/gain weight= 3): "],
        "target":[float,"weekly target(kg): "]}

    for k,v in user_input.items():
        user_input[k][1] = input(v[1])
    return user_input

def check_validation(user_input):  
    for k,v in user_input.items():
        while True:
            try:
                val_type = v[0]
                if k == "sex":
                    if val_type(v[1]) not in ["male","female"]:
                        raise ValueError
                    else:
                        user_input[k] = val_type(v[1])
                elif k == "activity":
                    if val_type(v[1]) not in [1,2,3,4]:
                        raise ValueError
                    else:
                        user_input[k] = val_type(v[1])
                elif k == "goal":
                    if val_type(v[1]) not in [1,2,3]:
                        raise ValueError
                    else:
                        user_input[k] = val_type(v[1])
                else:
                    user_input[k] = val_type(v[1])
                break
            except ValueError:
                raise ValueError("Invalid Input. Try agian.")
    return user_input

def choose_function(calculator): 
    menu = {"1": calculator.bmr,
            "2": calculator.maintenance_tdee, 
            "3": calculator.weightloss_tdee,
            "4": calculator.weightgain_tdee,
            "5": sys.exit}
    print("1. get bmr")
    print("2. get maintenance TDEE")
    print("3. get weight loss TDEE")
    print("4. get weight gain TDEE")
    print("5. exit")
    user_input = input("Please select menu: ")
    clear_screen()
    if user_input == "5":
        menu[user_input](0)
    else:
        return menu[user_input]

def clear_screen():
    if os.name == "nt":
        command = "cls"
    else:
        command = "clear"
    subprocess.run(command, shell=True)

def main(): 
    User_Manager = UserManager()

    ###get mail from user and check if valid then check user database
    email = input("Please enter your email: ")
    User_Manager.check_valid_email(email)
    found_user = User_Manager.search_user_database(email)

    if not found_user:
            raw_userdata = get_user_data()
            valid_userdata = check_validation(raw_userdata)
            User_Manager.store_user(email,valid_userdata)
            user = User(**valid_userdata)
            calculator = CALculator(user)
            
    elif found_user:
        userdata = User_Manager.get_user_info(email)
        user = User(**userdata)
        calculator = CALculator(user)

    while True:
        clear_screen()
        print(choose_function(calculator))
        print("Press 'Back Space' to go back")
        keyboard.wait("backspace")


if __name__ == "__main__":
      main()
    