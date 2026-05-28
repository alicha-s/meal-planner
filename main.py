from typing import Literal
import sys,os

class User:
    def __init__(self,name,age,weight,height,sex,activity,goal,target):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.activity = activity
        self.goal = goal
        self.target = target

    @property
    def bmr(self):
        if self.sex == "male":
            return round((10*self.weight)+(6.25*self.height)-(5*self.age)+5)
        else:
            return round((10*self.weight)+(6.25*self.height)-(5*self.age)-161)
        
    @property
    def maintenace_tdee(self):
        if self.activity == 1:
            return round(self.bmr * 1.2)
        elif self.activity == 2:
            return round(self.bmr * 1.375)
        elif self.activity == 3:
            return round(self.bmr * 1.55)
        elif self.activity == 4:
            return round(self.bmr * 1.725)
    
    @property
    # DCD: Daily Calorie Deficiet, TC: Target Calorie
    def weightloss_tdee(self):
        DCD = (7700*self.goal)/7
        TC = self.maintenace_tdee - DCD
        percentage = (DCD/self.tdee)*100
        if percentage > 20:
            return "not sustainable"
        return TC

    @property
    def weightgain_tdee(self):
        DCD = (7700*self.goal)/7
        TC = self.maintenace_tdee + DCD
        percentage = (DCD/self.maintenace_tdee)*100
        if percentage > 20:
            return "not sustainable"
        return TC

def create_user():
    user_input = {"name":[str,"Name: "],
        "age":[int,"Age: "],
        "weight":[int,"Weight(kg): "],
        "height":[int,"Height(cm): "],
        "sex":[str,"Sex(male/female): "],
        "activity":[int,"Activity(Please input number 1~4\nSedentary= 1/Lightly Active= 2/Moderately Active= 3/Very Active= 4): "],
        "goal":[int,"Goal(Please input number 1~3\nlose weight= 1/maintain= 2/gain weight= 3): "],
        "target":[float,"weekly target(kg): "]}

    for k,v in user_input.items():
        valid = True
        while valid:
            try:
                user_input[k] = check_validation(k,v[0],input(v[1]))
                valid = False
            except:
                print("Invalid Input. Try agian.")

    user = User(**user_input)

def check_validation(key,val_type,value):  
    if key == "sex":
        if val_type(value) not in ["male","female"]:
            raise ValueError
    elif key == "activity":
        if val_type(value) not in [1,2,3,4]:
            raise ValueError
    elif key == "goal":
        if val_type(value) not in [1,2,3]:
            raise ValueError
    else:
        return val_type(value)

def main():
    create_user()

if __name__ == "__main__":
    main()