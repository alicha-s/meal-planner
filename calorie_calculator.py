from create_user import User

class CALculator:
    def __init__(self,user):
        self.user = user

    @property
    def bmr(self):
        if self.user.sex == "male":
            return round((10*self.user.weight)+(6.25*self.user.height)-(5*self.user.age)+5)
        else:
            return round((10*self.user.weight)+(6.25*self.user.height)-(5*self.user.age)-161)

    @property 
    def maintenace_tdee(self):
        if self.user.activity == 1:
            return round(self.bmr * 1.2)
        elif self.user.activity == 2:
            return round(self.bmr * 1.375)
        elif self.user.activity == 3:
            return round(self.bmr * 1.55)
        elif self.user.activity == 4:
            return round(self.bmr * 1.725)
    

    # DCD: Daily Calorie Deficiet, TC: Target Calorie
    def weightloss_tdee(self):
        DCD = (7700*self.user.target)/7
        TC = self.maintenace_tdee - DCD
        percentage = (DCD/self.maintenace_tdee)*100
        if percentage > 20:
            print(f"{self.user.target} per week is not sustainable. Target calories is too low.")
        return TC


    def weightgain_tdee(self):
        DCD = (7700*self.user.target)/7
        TC = self.maintenace_tdee + DCD
        percentage = (DCD/self.maintenace_tdee)*100
        if percentage > 20:
            print(f"{self.user.target} per week is not sustainable. Target calories is too high.")
        return TC