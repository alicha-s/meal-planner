from pydantic import BaseModel,ValidationError
from typing import Literal
import sys,os

class User(BaseModel):
    name: str
    age: int
    weight: int
    height: int
    sex: Literal["male","female"]
    activity: Literal["Sedentary","Lightly Active","Moderately Active","Very Active"]
    goal: Literal["lose weight","maintain","gain weight"]
    target: float

    @classmethod
    def get_input(cls):
        while True:
            user_input = {"name":"Name: ",
                "age":"Age: ",
                "weight":"Weight(kg): ",
                "height":"Height(cm): ",
                "sex":"Sex(male/female): ",
                "activity":"Activity(Sedentary/Lightly Active/Moderately Active/Very Active): ",
                "goal":"Goal(lose weight/maintain/gain weight): ",
                "target":"weekly target(kg): "}
            
            args = {}
            for k,v in user_input.items():
                args[k] = input(v)
            
            try:
                user = cls(**user_input)
                return user
            except ValidationError as e:
                print(e)

    @property
    def bmr(self):
        if self.sex == "male":
            return round((10*self.weight)+(6.25*self.height)-(5*self.age)+5)
        else:
            return round((10*self.weight)+(6.25*self.height)-(5*self.age)-161)
        
    @property
    def maintenace_tdee(self):
        if self.activity == "Sedentary":
            return round(self.bmr * 1.2)
        elif self.activity == "Lightly Active":
            return round(self.bmr * 1.375)
        elif self.activity == "Moderately Active":
            return round(self.bmr * 1.55)
        elif self.activity == "Very Active":
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
    user = User.get_input()

def main():
    create_user()

if __name__ == "__main__":
    main()