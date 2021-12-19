#Skillcards
from random import choice, randint

class Skillcards:
    def get_description(self, key):
        return(self.results[key])
    def use(self, attacker, defender):  
        score = self.roll_attack(attacker, defender)
        maped_score = self.get_attack_result(score)
        self.attack_effect(maped_score, attacker, defender)
        #print(self.get_result_description())  #checking effects <--- for test purposes/ not  4 production
        
    def get_result_description(self):
        return(self.result_description)
    def get_basedescription(name, rarity, quantity, cost):
        return(str(f"{name.upper()}\nx{quantity} collected ({rarity})\nenergy cost: {cost}"))
      
class Standupcards(Skillcards):
    standup = True


class Groundcards(Skillcards):
    standup = False
    
class Jab(Standupcards):
    def __init__(self):
        self.name = "Jab"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill =  False
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your boxing, opponent boxing\neffects(4 rolls):\
        \n4 success: apply DAMAGE, points\
        \n3,2 success: points\
        \n0 successes: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "What a jab!",
            "success": "scored some points",
            "defeat" : "jab, jab, miss, miss",
            "lose"   : "can't even punch correctly..."}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(4):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"4":"win", "3": "success","2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            attacker.points += 1
            defender.got_hurt()
        elif maped_score == "success":
            attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
    

class Lowkick(Standupcards):
    def __init__(self):
        self.name = "Lowkick"
        self.rarity = "common"
        self.quantity = 1 
        self.grapplingskill =  False
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your muaythai, opponent muaythai, 3 rolls\neffects:\
        \n3 success: apply TIRED, points\
        \n2 success: points\
        \n0 successes: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "that lowkick could have broken a bone!",
            "success": "on target",
            "defeat" : "nothing there",
            "lose"   : "pathetic kick..."}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            attacker.points += 1
            defender.got_tired()
        elif maped_score == "success":
            attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
            

class Pullguard(Standupcards):
    def __init__(self):
        self.name = "Pull Guard"
        self.rarity = "uncommon"
        self.quantity = 1
        self.grapplingskill = True
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent wrestling, 2 rolls\neffects:\
        \n2,1 success: TAKEDOWN, reduce points\
        \n0 successes: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "he's pullin the guard. What a move!",
            "success": "he is pulling a guard.",
            "defeat" : "",
            "lose"   : "he's trying to pull the guard... but opponent refuses to get involved!"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        self.result_description = self.results[maped_score]
        global STANDUP
        if maped_score == "win":
            attacker.points -= 1
            STANDUP=False
        elif maped_score == "success":
            attacker.points -= 1
            STANDUP=False
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1


class Bearhug_Takedown(Standupcards):
    def __init__(self):
        self.name = "Bearhug takedown"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill = True
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your wrestling, opponent wrestling, 2 rolls\neffects:\
        \n2 success: TAKEDOWN, points*2\
        \n0 successes: get DAMAGE or TAKEDOWN with GROUNDCONTROL for opponent, reduce points"
        return(result)
    def all_results(self):
        results ={
            "win"    : "What a beautiful oldschool takedown!",
            "success": "",
            "defeat" : "No luck with that risky move",
            "lose"   : "He's turning back from the oponent! He got countered!"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "defeat",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        self.result_description = self.results[maped_score]
        global STANDUP
        if maped_score == "win":
            attacker.points += 2
            STANDUP=False
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
            if choice(["boom", "ground"]) == "ground":
                STANDUP=False
                defender.groundcontrol = True         
            else: attacker.got_hurt()
        
        

class One_Two_Kick_Combo(Standupcards):
    def __init__(self):
        self.name = "1-2-kick combo"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill = False
        self.cost = 3
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your box+mt, opponent box+mt, 2 rolls\neffects:\
        \n2 success: apply ROCKED, points*2\
        \n1 success: points\
        \n0 successes: no effect"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Boom! And one more!",
            "success": "Partially on target",
            "defeat" : "",
            "lose"   : "Nothing landed"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_2_stat(attacker.boxing, attacker.muay_thai, defender.boxing, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        self.result_description = self.results[maped_score]
        global STANDUP
        if maped_score == "win":
            attacker.points += 2
            defender.got_rocked()
        elif maped_score == "success":
            attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass


class Powerjab(Jab):
    def __init__(self):
        self.name = "Power jab"
        self.rarity = "uncommon"
        self.quantity = 1
        self.grapplingskill =  False
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your boxing, opponent boxing\neffects(2 rolls):\
        \n2 success: apply DAMAGE, points\
        \n1 success: points(50% chance)\
        \n0 successes: reduce points(50% chance)"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "What a jab! Opponent felt that one!",
            "success": "opponent tagged",
            "defeat" : "",
            "lose"   : "This lefthand was visible from a kilometer..."}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            attacker.points += 1
            defender.got_hurt()
        elif maped_score == "success":
            if choice(["points", "no"]) == "points":
                attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            if choice(["lostpoints", "no"]) == "lostpoints":
                attacker.points -= 1

############################################################  to be implemented ---> check GROUNDCONTROL before USE
class Lay_And_Pray(Groundcards):
    def __init__(self):
        self.name = "Lay and pray"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill =  True
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj,wrestling, opponent bjj,wrestling\neffects(1 roll):\
        \n1 success: TIME LAPSE\
        \n0 success: STANDUP\
        \nWORKS ONLY IF OPPONENT DOES NOT HAVE GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "he is successfully blocking any opponent move",
            "success": "",
            "defeat" : "",
            "lose"   : "Refree have to stop that sweat fest"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_2_stat(attacker.bjj, attacker.wrestling, defender.bjj, defender.wrestling))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"1":"win", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        global TIMER
        global STANDUP
        if maped_score == "win":
            TIMER += 1
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            STANDUP = True
            

class Brute_Force_Sweep(Groundcards):
    def __init__(self):
        self.name = "Brute force sweep"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill =  True
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent bjj\neffects(1roll):\
        \n1 success: release opponent GROUNDCONTROL or get GROUNDCONTROL\
        \n0 success: additional energy cost(1)"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He sweeps opponent. No technique here, but it works!",
            "success": "",
            "defeat" : "",
            "lose"   : "why bother with any technique if you have muscles? Dude, opponent is not a bag of potatoes"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"1":"win",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            if defender.groundcontrol:
                defender.groundcontrol = False
            elif attacker.groundcontrol:
                attacker.points += 1
            else:
                attacker.groundcontrol = True      
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.energy -= 1


class Illegal_Move_Trap(Groundcards):           #####  add another check to use this skill after eot "lost" evaluation; test effect
    def __init__(self):
        self.name = "Illegal move trap"
        self.rarity = "rare"
        self.quantity = 1
        self.grapplingskill =  False
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \nIf the fight should be lost before the decision:\
        \n50% that fight is not lost. Instead continue the fight\
        \n(GROUNDCONTROL, TIRED, ROCKED effects are still in place)"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "It was an eye poke, wasn't it?",
            "success": "",
            "defeat" : "",
            "lose"   : "the fight is over and he is still arguing with the refree!"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = False
        for _ in range(1):
            if choice(["illegal", "no"]) == "illegal":
                return("1")          
        return("0")
    
    def get_attack_result(self, score):
        mapping = {"1":"win",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):   #### test it; 
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            attacker.lost = False
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass
            
            
class Roar_Naked_Choke(Groundcards):  #############################################
    def __init__(self):
        self.name = "Roar naked choke"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill =  True
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent bjj\neffects(1roll):\
        \n1 success: WIN if you have GROUNDCONTROL, otherwise points\
        \n0 success: lose GROUNDCONTROL(25%), TIME LAPSE(25%)\
        \nCAN'T BE PLAYED IF OPPONENT HAVE GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He's applying RNC... will it be over?",
            "success": "",
            "defeat" : "",
            "lose"   : "failed to control opponent, does he go for a leg?"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"1":"win",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            if attacker.groundcontrol:
                defender.lost = True
            else:
                attacker.points += 1     
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            if randint(1, 4) == 1:             
                attacker.groundcontrol = False
            if randint(1, 4) == 1:
                global STANDUP
                STANDUP = True           


class Lucky_Punch(Standupcards):
    def __init__(self):
        self.name = "Lucky Punch"
        self.rarity = "rare"
        self.quantity = 1
        self.grapplingskill =  False
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: RANDOM roll vs opponent box or mt\neffects(1 roll):\
        \n1 success: apply at random: (no effect, points, TIRED, DAMAGE, ROCKED)\
        \nchance for TAKEDOWN (15%)"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "That was clearly a lucky punch",
            "success": "",
            "defeat" : "",
            "lose"   : "No luck you gambler"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            attacker_stat = defender.boxing//3 +defender.muay_thai//3 + 4
            defender_stat = choice([defender.boxing, defender.muay_thai]) + 1
            result.append(attacker.roll_1_stat(attacker_stat, defender_stat))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            result = choice(["rocked", "no effect", "tired", "damage","points"])
            if result == "rocked":
                defender.got_rocked()
            elif result == "tired":
                defender.got_tired()
            elif result == "damage":
                defender.got_hurt()
            elif result == "points": 
                attacker.points += 1
            global STANDUP
            if randint(1, 7) == 7:
                STANDUP = False
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass        


class Granite_Chin(Standupcards):
    def __init__(self):
        self.name = "Granite chin"
        self.rarity = "uncommon"
        self.quantity = 1
        self.grapplingskill = False
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: none \neffects:\
        \nRemoves ROCKED effect\
        \nadds 1 energy (50% chance)\
        \nWORKS ONLY IF YOU ARE ROCKED"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "His chin is unbreakable!",
            "success": "The blows do not impress him at all",
            "defeat" : "",
            "lose"   : ""}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(10, 10))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"1":"win", "0": "success"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        self.result_description = self.results[maped_score]
        global STANDUP
        if maped_score == "win":
            attacker.rocked = False
            attacker.energy += 1
        elif maped_score == "success":
            attacker.rocked = False
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass



class Cardio_King(Standupcards):
    def __init__(self):
        self.name = "Cardio king"
        self.rarity = "common"
        self.quantity = 1
        self.grapplingskill = False
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: none \neffects:\
        \nRemoves TIRED effect\
        \nadds 1 energy (50% chance)\
        \nWORKS ONLY IF YOU ARE TIRED"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He is gassing out? Not at all!",
            "success": "Some avoidance tactics, and he's looking refreshed now.",
            "defeat" : "",
            "lose"   : ""}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(10, 10))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"1":"win", "0": "success"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        self.result_description = self.results[maped_score]
        global STANDUP
        if maped_score == "win":
            attacker.energy += 1
            attacker.tired = False
        elif maped_score == "success":
            attacker.tired = False
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass
        
        
############################################################### here I can get all the Skillcards name :)
#import pyclbr
#module_name = 'Skillcards'
#module_info = pyclbr.readmodule(module_name)
##print(module_info)

#for item in module_info.values():
    #print(item.name)
    

#some untired card /  universal TIRED
#sth that lowers boxing and mt
#sth that lowers bjj, wrestlin

#slap --> worse  jab :P
#killer kick
#high kick
#wild exchange --> both got damaged
#lucky punch
#devastating_overhand
#windmill_style
#butthead
#knee_from_clinch
#elbow
#flying knee
#superman punch
#Dirty_boxing

#One_leg_takedown
#Double_Leg   --> get punched if op. muaythai
#suplex
#Kata-guruma
#Sweep_trip_throw

#universal punch --> both standup and ground

#mount position --> groundcontrol/punch
#slam
#guilotine --> tired you/him/ submission
#armbar
#heel hook
#triangle
#Escape!
#GnP
#cheap shots --> points on the ground
#hammer fist
#drunkenjitsu --> ground action better when tired