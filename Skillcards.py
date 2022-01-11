#Skillcards
from random import choice, randint


class Skillcards:
    def get_description(self, key):
        return(self.results[key])
    def use(self, attacker, defender):  
        score = self.roll_attack(attacker, defender)
        maped_score = self.get_attack_result(score)
        attacker.update_possible_victory_details(*self.win_descriptions(maped_score)) 
        self.result_description = self.results[maped_score]
        attacker.currentfight.prompt_fight_info(self.get_result_description(), action=self.name)
        self.attack_effect(maped_score, attacker, defender)
        #print(self.get_result_description())  #checking effects <--- for test purposes/ not  4 production
        
    def get_result_description(self):
        return(self.result_description)
    def get_basedescription(name, rarity, quantity, cost):
        return(str(f"{name.upper()}\nx{quantity} collected ({rarity})\nenergy cost: {cost}"))
    def win_descriptions(self, maped_score):
        result = {}
        return(result.get(maped_score,["N/A", "N/A"]))    
    
class Standupcards(Skillcards):
    restriction = ["standup"]

class Groundcards(Skillcards):
    restriction = ["ground"]
   
    
    
class Jab(Standupcards):
    def __init__(self):
        self.name = "Jab"
        self.rarity = "common"
        self.quantity = 1
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
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "punch"]}
        return(result.get(maped_score,["N/A", "N/A"]))
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(4):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"4":"win", "3": "success","2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
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
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "leg injury"]}
        return(result.get(maped_score,["N/A", "N/A"]))
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
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
        self.name = "Pull guard"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent wrestling, 2 rolls\neffects:\
        \n2 success: TAKEDOWN, reduce points\
        \n1 success: TAKEDOWN, op GROUNDCONTROL, reduce points\
        \n0 successes: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "he's pullin the guard. What a move!",
            "success": "he is pulling a guard... risky move!",
            "defeat" : "",
            "lose"   : "he's trying to pull the guard... but opponent refuses to get involved!"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {}
        return(result.get(maped_score,["N/A", "N/A"]))    
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
            defender.groundcontrol = True
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1



class Bearhug_Takedown(Standupcards):
    def __init__(self):
        self.name = "Bearhug takedown"
        self.rarity = "common"
        self.quantity = 1
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
    
    def win_descriptions(self, maped_score):
        result = {"lose":["TKO", "punches"]}
        return(result.get(maped_score,["N/A", "N/A"]))        
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "defeat",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points += 2
            attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
            if choice(["boom", "ground"]) == "ground":
                attacker.currentfight.setStandup(False)
                defender.groundcontrol = True         
            else: attacker.got_hurt()
        
        

class One_Two_Kick_Combo(Standupcards):
    def __init__(self):
        self.name = "1-2-kick combo"
        self.rarity = "common"
        self.quantity = 1
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
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "kicks and punches"]}
        return(result.get(maped_score,["N/A", "N/A"]))        
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_2_stat(attacker.boxing, attacker.muay_thai, defender.boxing, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success",  "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
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
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "punch"]}
        return(result.get(maped_score,["N/A", "N/A"]))        
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
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
        if maped_score == "win":
            attacker.currentfight.moveTimer()
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.currentfight.setStandup(True)
            

class Brute_Force_Sweep(Groundcards):
    def __init__(self):
        self.name = "Brute force sweep"
        self.rarity = "common"
        self.quantity = 1
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
    # we have to overcome DESCRIBTION ERROR(it overrides the fight result attribute - we need to activate it differently )
    def __init__(self):
        self.name = "Illegal move trap"
        self.rarity = "rare"
        self.quantity = 1
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
        if maped_score == "win":
            attacker.lost = False
            attacker.currentfight.matchresult = ["victorytype", "victorymethod"]
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass
            
            

class Lucky_Punch(Standupcards):
    def __init__(self):
        self.name = "Lucky Punch"
        self.rarity = "rare"
        self.quantity = 1
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
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "(lucky)punch"]}
        return(result.get(maped_score,["N/A", "N/A"]))  
    
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
            if randint(1, 7) == 7:
                attacker.currentfight.setStandup(False)
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
            "win"    : "His chin is unbreakable! He recovered!",
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
        if maped_score == "win":
            attacker.energy += 1
            attacker.tired = False
        elif maped_score == "success":
            attacker.tired = False
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass



class Swing_For_The_Fences(Standupcards):
    def __init__(self):
        self.name = "Swing for the fences"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 3
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your & op box, muaythai, wrestling \neffects(3 rolls):\
        \n3 success: opponent ROCKED\
        \n2 success: opponent DAMAGED, 25% you DAMAGED\
        \n1 success: you DAMAGED, 25% op DAMAGED\
        \n0 success: you ROCKED\
        \nchance for TAKEDOWN (~15%)"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "What a decision! He started a brawl and wow, he can finish it now!",
            "success": "What an exchange, he is winning it!",
            "defeat" : "I would not recommend going for this exchange...",
            "lose"   : "He just've got rooocked! What a beating!"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "kicks and punches"],
                  "success":["TKO", "punches"],
                  "defeat":["TKO", "punches"],
                  "lose":["KO", "kicks and punches"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))    
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            at = [attacker.boxing, attacker.muay_thai, attacker.wrestling]
            df = [defender.boxing, defender.muay_thai, defender.wrestling]
            result.append(attacker.roll_1_stat(choice(at), choice(df)))
            result.append(attacker.roll_1_stat(choice(at), choice(df)))
            result.append(attacker.roll_1_stat(choice(at), choice(df)))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win","2":"success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            defender.got_rocked()
        elif maped_score == "success":
            defender.got_hurt()
            if choice("damage", "no") == "damage":
                attacker.got_hurt()            
        elif maped_score == "defeat":
            attacker.got_hurt()
            if choice("damage", "no") == "damage":
                defender.got_hurt()
        elif maped_score == "lose":
            attacker.got_rocked()    
        if randint(1, 7) == 7:
            attacker.currentfight.setStandup(False)
        


class Windmill_Style(Standupcards):
    def __init__(self):
        self.name = "Windmill Style"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 4
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your muaythai, op boxing \n(2 rolls)effects:\
        \n2 success: apply DAMAGE, points\
        \n1 success: apply DAMAGE(33% chance)\
        \n0 success: got TIRED, suffer DAMAGE"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He is like a hurricane... he discovers technique on the fly and rains that wide punches. Storm of chaos incoming!",
            "success": "Pub brawl here!",
            "defeat" : "",
            "lose"   : "Oh boy! Few swings and he totally gassed out"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "punches"],
                  "success":["TKO", "punches"],
                  "lose":["TKO", "retirement"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))    
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win","1":"success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            defender.got_hurt()
            attacker.points += 1
        elif maped_score == "success":
            if choice("damage", "no", "no") == "damage":
                defender.got_hurt()            
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.got_hurt()
            attacker.got_tired()
            


class Slap(Standupcards):
    def __init__(self):
        self.name = "Slap"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: 1 random, 1 box vs mt , 1 box vs box roll\neffects(3 rolls):\
        \n3 success: points, funny description\
        \n2 success: points(50% chance), funny description\
        \n1 successes: funny description\
        \n0 successes: reduce points, funny description\
        "
        return(result)
    
    def all_results(self):
        funny_win = choice(["Slap that bitch! Yeah! One more time, he's likin it!",
                            "Me gusta you bastrad!",
                            "Boom and I see a tear! He was schooled and he'll cry us a river", 
                            "That was thai-chi move. He zapped all willpower out him",
                            "Nick Diaz classes wasn't wasted here. They were smoking some goood shit together",
                            "He showed him whos the daddy here. Naughty-naught boy have to suffer!",
                            "Punch like Neo from Matrix... like Tyler from Fight Club... or just like a really fucked up grrrl!"
                            ])
        funny_lose = choice(["Are u kiddin me bro? What's next? You'll be rolling on the floor like one of that jiujitsu gays... i mean guys?",
                             "He is fighting invisible flies... What a predator!",
                             "He was clearly learning boxing from books",
                             "Ke? He was ordering a burrito with that karate-waving?",
                             "My granny can do it better. She can give him a lesson or two!",
                             "Wide swings, wide wings. If he is sober i have to drink"
                             ])
        results ={
            "win"    : funny_win,
            "success": funny_win,
            "defeat" : funny_lose,
            "lose"   : funny_lose}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.muay_thai))
            result.append(attacker.roll_1_stat(10, 10))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        self.result_description = self.results[maped_score]
        if maped_score == "win":
            attacker.points += 1
        elif maped_score == "success":
            if choice(["points", "no"]) == "points":
                attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1



class Highkick(Standupcards):
    def __init__(self):
        self.name = "Highkick"
        self.rarity = "uncommon"
        self.quantity = 1 
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your muaythai, opponent muaythai(2), boxing(1), 3 rolls\neffects:\
        \n3 success: apply ROCKED, 25% TAKEDOWN, 25% DAMAGE, points*2\
        \n2 success: apply DAMAGE, points\
        \n0 successes: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Foot landed directly on the chin! Is it over?",
            "success": "Kick and boom, partially landed!",
            "defeat" : "opponent stepped back and dodged the leg.",
            "lose"   : "Oponent laughs, refree as well"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "highkick"],
                  "success":["TKO", "highkick"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))        
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points += 2
            defender.got_rocked()
            if randint(1,4) == 4:
                defender.got_hurt()            
            if randint(1,4) == 4:
                attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            attacker.points += 1
            defender.got_hurt() 
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
     


class Flying_Knee(Standupcards):
    def __init__(self):
        self.name = "Flying knee"
        self.rarity = "rare"
        self.quantity = 1 
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your muaythai, opponent muaythai, boxing, 2 rolls\neffects:\
        \n2 success: apply DAMAGE, apply DAMAGE, points\
        \n1 success: apply TIRED, points\
        \n0 successes: TAKEDOWN, opponent GROUNDCONTROL, reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Opponent head was low. That knee hit him like a truck.",
            "success": "Knee to the midsection",
            "defeat" : "",
            "lose"   : "Going for a kneee... but opponent is moving out of the way... He's going for a counter and he pins kangaroo down to the mat. "}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "flying knee"],
                  "success":["Submission", "knee"]
                  }
        return(result.get(maped_score,["N/A", "N/A"])) 
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.boxing))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points += 1
            defender.got_hurt()
            defender.got_hurt() 
        elif maped_score == "success":
            attacker.points += 1
            defender.got_tired() 
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.currentfight.setStandup(False)
            defender.groundcontrol = True
            attacker.points -= 1
            


        
class Roar_Naked_Choke(Groundcards):  ##################GROUNDCONTROL restriction###########################
    def __init__(self):
        self.name = "Roar naked choke"
        self.rarity = "common"
        self.quantity = 1
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
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "roar naked choke"]}
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"1":"win", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if attacker.groundcontrol:
                defender.fightlost()
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
                attacker.currentfight.moveTimer()


class Armbar(Groundcards): 
    def __init__(self):
        self.name = "Armbar"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent bjj\neffects(3roll):\
        \n3 success: WIN if GROUNDCONTROL, otherwise apply GROUNDCONTROL, points\
        \n2 success: if GROUNDCONTROL:apply DAMAGE(50%),points else: apply GROUNDCONTROL\
        \n1 success: random: suffer DAMAGE, lose GROUNDCONTROL, op GROUNDCONTROL, reduce points or STANDUP\
        \n0 success: lose GROUNDCONTROL, opponent GROUNDCONTROL or STANDUP, reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He is going for straight armbar and it can work!",
            "success": "He tries armbar and sweep his opponent instead!",
            "defeat" : "He attacked arm and failed.",
            "lose"   : "What a poor technique..."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "armbar"],
                  "success":["TKO", "punches(GnP)"],
                  "defeat":["TKO", "punches(GnP)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win",  "2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if attacker.groundcontrol:
                defender.fightlost()
            else:
                attacker.points += 1     
        elif maped_score == "success":
            if attacker.groundcontrol:
                effect = choice("no", "dmg")
                if effect == "dmg": 
                    defender.got_hurt()
                    attacker.points += 1
            else: 
                attacker.groundcontrol = True
        elif maped_score == "defeat":
            effect = choice(["dmg", "loseground", "oground", "rpoints", "standup"])
            if effect == "dmg": attacker.got_hurt()
            elif effect == "loseground": attacker.groundcontrol = False
            elif effect == "oground": defender.groundcontrol = True
            elif effect == "rpoints": attacker.points -= 1
            elif effect == "standup": attacker.currentfight.setStandup(True)
        elif maped_score == "lose":
            attacker.groundcontrol = False
            effect = choice(["standup", "ground"])
            if effect == "standup": attacker.currentfight.setStandup(True)
            elif effect == "ground": defender.groundcontrol = True
            attacker.points -= 1



class Ground_and_Pound(Groundcards): 
    def __init__(self):
        self.name = "Ground and pound"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 3
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj,wrestling,boxing  opponent bjj\neffects(3roll):\
        \n3 success: apply ROCKED if GROUNDCONTROL, otherwise DAMAGE, points*2\
        \n2 success: apply DAMAGE if GROUNDCONTROL, points\
        \n1 success: TIMELAPSE\
        \n0 success: lose GROUNDCONTROL, opponent GROUNDCONTROL, reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He's raining punches from the top and looking for a finish!",
            "success": "ribs, ribs and chin, he is pushing his adventage.",
            "defeat" : "few insignificant punches, most of them blocked",
            "lose"   : "It is why you do not play on the ground with bjj shark..."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "punches(GnP)"],
                  "success":["TKO", "punches(GnP)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))  
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win",  "2": "success", "1":"defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if attacker.groundcontrol:
                defender.got_rocked()  
            else: defender.got_hurt()
            attacker.points += 2     
        elif maped_score == "success":
            if attacker.groundcontrol:
                defender.got_hurt()
            attacker.points += 1 
        elif maped_score == "defeat":
            attacker.currentfight.moveTimer()  
        elif maped_score == "lose":
            attacker.groundcontrol = False
            defender.groundcontrol = True
            attacker.points -= 1



class Dirty_Boxing(Standupcards):
    def __init__(self):
        self.name = "Dirty boxing"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your/op's boxing and wrestling \neffects(2 roll):\
        \n2 success: apply DAMAGE, points\
        \n1 success: apply DAMAGE(25% chance)\
        \n0 success: got DAMAGE (25% chance)"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He's controlling opponent against the cage and pointing with punches!",
            "success": "Stalemate in the clinch... Oh in fact, he is scoring something here",
            "defeat" : "",
            "lose"   : "he eats punches more then he throws"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "punches(clinch)"],
                  "success":["TKO", "punches(clinch)"],
                  "lose": ["TKO", "punches(clinch)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))      
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_2_stat(attacker.boxing, attacker.wrestling, defender.boxing, defender.wrestling))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.got_hurt()
            attacker.points += 1
        elif maped_score == "success":
            if choice(["score", "no", "no", "no"]) == "score":
                defender.got_hurt()
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            if choice(["score", "no", "no", "no"]) == "score":
                attacker.got_hurt()       


class Devastating_Overhand(Standupcards):
    def __init__(self):
        self.name = "Devastating overhand"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your boxing, op boxing & muay thai\neffects(2 roll):\
        \n2 success: apply ROCKED, points*2, TAKEDOWN(50% chance)\
        \n0 success: got DAMAGE,"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Nasty right hand over the top! That's a knockout, right?",
            "success": "That one was damn close. Few more centimeters and we would see a KO.",
            "defeat" : "",
            "lose"   : "Haymaker got countered by opponent"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "punch(overhand right)"],
                  "success":["TKO", "punch(overhand right)"],
                  "lose": ["TKO", "punch"]
                  }
        print(result.get(maped_score,["N/A", "N/A"]))
        return(result.get(maped_score,["N/A", "N/A"]))      
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.got_rocked()
            attacker.points += 2
            if choice(["takedown", "no"]) == "takedown":
                attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.got_hurt()   


class Elbows(Standupcards):
    def __init__(self):
        self.name = "Elbows"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: muay thai\neffects(2 roll):\
        \n2 success: apply DAMAGE*2, points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He cuts opponent with an elbow!",
            "success": "",
            "defeat" : "He is trying to close the distance, but can't",
            "lose"   : "He won't achieve much with that questionable elbows"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "elbows"]}
        return(result.get(maped_score,["N/A", "N/A"]))   
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win", "1": "defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.got_hurt()
            defender.got_hurt()
            attacker.points += 1
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass  
        
        
        
class Flying_Armbar(Standupcards):
    def __init__(self):
        self.name = "Flying armbar"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your/op's bjj \neffects(3 roll):\
        \n3 success: WIN the fight\
        \n2 success: TAKEDOWN, op GROUNDCONTROL(50%), points\
        \n1 success: TAKEDOWN, op GROUNDCONTROL, reduce points\
        \n0 success: reduce points*2"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Flying armbar? Are you kidding me? What a finish!",
            "success": "Flying armbar attempt? Crowd is loooving it!",
            "defeat" : "Kangaroo tried some fancy technique and finished pinned to the ground.",
            "lose"   : "I don't know what he was trying to achieve, but I cannot stop laughing"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "flying armbar"]}
        return(result.get(maped_score,["N/A", "N/A"]))       
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1": "defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.fightlost()  
        elif maped_score == "success":
            attacker.points += 1
            attacker.currentfight.setStandup(False)
            if choice(["lostposition", "no"]) == "lostposition":
                defender.groundcontrol = True           
        elif maped_score == "defeat":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
            defender.groundcontrol = True 
        elif maped_score == "lose":
            attacker.points -= 2


class Double_Leg(Standupcards):
    def __init__(self):
        self.name = "Double leg"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 3
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your wrestling(2),bjj(1), op wrestling(2),muaythai(1)\neffects(3 roll):\
        \n3 success: TAKEDOWN, GROUNDCONTROL, points*2\
        \n2 success: TAKEDOWN, points\
        \n0 success: suffer DAMAGE, reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He charged like a roller! What a beautiful takedown. Please give him round of applause.",
            "success": "He ducks under opponent... and he gets it!",
            "defeat" : "He ducks under opponent... timed sprawl and he's pushed back",
            "lose"   : "He tried double leg and was countered!"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"lose": ["TKO", "knee"]}
        return(result.get(maped_score,["N/A", "N/A"]))       
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1": "defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 2
            attacker.currentfight.setStandup(False)
            attacker.groundcontrol = True 
        elif maped_score == "success":
            attacker.points += 1
            attacker.currentfight.setStandup(False)         
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.got_hurt()
            attacker.points -= 1



class Universal_Punch(Standupcards):               # we have to test restrictions 
    def __init__(self):
        self.name = "Universal punch"
        self.restriction = ["standup", "ground"] # only for unusual cards
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: boxing,muay thai\neffects(4 roll):\
        \n4,3 success: apply DAMAGE, points\
        \n2 success: points if GROUNDCONTROL\
        \n0 success: reduce points, lose GROUNDCONTROL, TAKEDOWN\
        CAN BE USED BOTH IN STANDUP AND ON THE GROUND"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "It connected! Opponent is in real trouble!",
            "success": "This man can strike from every angle and position... great... but does it really matter? These punches can't hurt a fly.",
            "defeat" : "Miss and... miss one more time. Next time he should try some standard stuff",
            "lose"   : "No, no and one more time no. Missed punched, missed opportunity, and now he is trouble."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "punch"]}
        return(result.get(maped_score,["N/A", "N/A"]))       
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(4):
            result.append(attacker.roll_2_stat(attacker.boxing, attacker.muay_thai, defender.boxing, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"4":"win",  "3":"win", "2":"success", "1": "defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 1
            defender.got_hurt()
        elif maped_score == "success":
            if attacker.groundcontrol:
                attacker.points += 1        
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.currentfight.setStandup(False)
            attacker.groundcontrol = False
            attacker.points -= 1


class Slam(Groundcards): 
    def __init__(self):
        self.name = "Slam"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 3
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your wrestling, opponent bjj,wrestling\neffects(2rolls):\
        \n2 success: apply ROCKED,GROUNDCONTROL, op lose GROUNDCONTROL, points*2\
        \n1 success: opponent lose GROUNDCONTROL\
        \n0 success: STANDUP"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Whaaaaaaaaaaaaaaaaat a slam!",
            "success": "He lifts opponent and drops him down.",
            "defeat" : "",
            "lose"   : "He lifts opponent who jumps down and fight move to the standup."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "slam"]}
        return(result.get(maped_score,["N/A", "N/A"]))   
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_2_stat(attacker.wrestling, attacker.wrestling, defender.wrestling, defender.bjj))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"2":"win",  "1": "success", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.got_rocked()
            defender.groundcontrol = False
            attacker.groundcontrol = True
            attacker.points += 2     
        elif maped_score == "success":
            defender.groundcontrol = False
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.currentfight.setStandup(True)



class Single_Leg(Standupcards):
    def __init__(self):
        self.name = "Double leg"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: wrestling\neffects(3 roll):\
        \n3 or 2 success: TAKEDOWN, points\
        \n0 success: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Perfectly executed single leg takedown lands into the halfguard. Please give him round of applause.",
            "success": "He catches the leg... and takes the fight to the mat.",
            "defeat" : "He catches the leg... but the opponent breaks the grip.",
            "lose"   : "He dives for the leg and he fails misarably."}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.muay_thai))
        return(str(sum(result )))
    
    def get_attack_result(self, score):
        mapping = {"3":"win", "2": "success", "1": "defeat", "0":"lose"}
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 1
            attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            attacker.points += 1
            attacker.currentfight.setStandup(False)        
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1

 
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

#killer kick
#butthead
#knee_from_clinch
#superman punch

#One_leg_takedown
#suplex
#Kata-guruma
#Sweep_trip_throw
#throw directly to the groundcontrol

#universal punch --> both standup and ground

#mount position --> groundcontrol/punch
#slam
#guilotine --> tired you/him/ submission
#heel hook
#triangle
#Escape!
#GnP
#cheap shots --> points on the ground
#vicous hammerfist
#drunkenjitsu --> ground action better when tired
#escape to standup
#reverse?