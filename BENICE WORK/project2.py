import re
class VotersID:
    def Serial_num(self):
        Serial_num = input("WELCOME FOR 2023 ELECTION PLEASE ENTER YOUR SERIAL NUMBER")
        if len(re.findall("[A-Za-z0-9.+@#$]", Serial_num))==6:
            print(f"Welcome! You have successfully logged in for 2023 Election")
        else:
            print(f"wrong pin_code number")


class Local_govt_election:
    APC = "NWOKEDI JOHN"
    PDP = "ANI SUNDAY"
    LP= "EMERE HOPE"
    def __init__(self, LG_result):
        self.LG_result = LG_result
    
        if LG_result == "NWOKEDI JOHN":
            print(f"In Local Government Election, you voted for APC ({LG_result})")
        elif LG_result == "ANI SUNDAY":
            print(f"In Local Government Election, you voted for PDP ({LG_result})")
        elif LG_result == "EMERE HOPE":
            print(f"In Local Government Election you voted for LP ({LG_result})")
        else: 
            print(f"Opps! invalid vote")
class State_govt_election:
    APC = "ENEMUO EKENE"
    PDP = "AYIM CHIBUZOR"
    LP= "ODOH BATHO"
    def __init__(self,SG_result):
        self.SG_result = SG_result
        if SG_result == "ENEMUO EKENE":
            print(f"In State Government Election, you voted for APC ({SG_result})")
        elif SG_result == "AYIM HIBUZOR":
            print(f"In State Government Election, you voted for PDP ({SG_result})")
        elif SG_result == "ODOH BATHO":
             print(f"In State Government Election, you voted for LP ({SG_result})")
        else: 
            print(f"Opps! invalid vote")
class federal_govt_election:
    APC = "TINUBU"
    PDP = "ATIKU ABUBARKAR"
    LP= "PETER OBI"
    def __init__(self,FG_result):
        self.FG_result = FG_result
    
        if FG_result == "TINUBU":
            print(f"In Federal Government Election, you voted for APC ({FG_result})")
        elif FG_result == "ATIKU ABUBARKAR":
            print(f"In Federal Government Election, you voted for PDP ({FG_result})")
        elif FG_result == "PETER OBI":
            print(f"In Federal Government Election, you voted for LP ({FG_result})")
        else: 
            print(f"Opps! {FG_result} is a wrong candidate and invalid vote")
                
            
obj = VotersID()
obj.Serial_num()
local = Local_govt_election(LG_result= (input("Enter your prefered candidate for local Govt Chairman")))
state = State_govt_election(SG_result =(input("Enter your prefered candidate for State Govt Chairman")))
federal = federal_govt_election(FG_result =(input("Enter your prefered candidate for Federal Govt Chairman")))
