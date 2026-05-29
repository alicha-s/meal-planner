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

    @classmethod
    def create_user(cls):
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
                    user_input[k] = cls.check_validation(k,v[0],input(v[1]))
                    valid = False
                except:
                    print("Invalid Input. Try agian.")
        return cls(**user_input)

    
    @staticmethod
    def check_validation(key,val_type,value):  
        if key == "sex":
            if val_type(value) not in ["male","female"]:
                raise ValueError
            else:
                return val_type(value)
        elif key == "activity":
            if val_type(value) not in [1,2,3,4]:
                raise ValueError
            else:
                return val_type(value)
        elif key == "goal":
            if val_type(value) not in [1,2,3]:
                raise ValueError
            else:
                return val_type(value)
        else:
            return val_type(value)
        
        # if registered user, fetch user data
        def get_registered_uesr(self):
            pass