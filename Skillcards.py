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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose","defeat","success","success","win")
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
            "win"    : "That lowkick could have broken a bone!",
            "success": "On target",
            "defeat" : "Nothing there",
            "lose"   : "Pathetic kick..."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "leg injury"]}
        return(result.get(maped_score,["N/A", "N/A"]))
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat","success", "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
            defender.get_groundcontrol() 
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "win")
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
                defender.get_groundcontrol()        
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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


class Lay_And_Pray(Groundcards):
    def __init__(self):
        self.name = "Lay and pray"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        restriction = ["ground", "OP_NO_groundcontrol"]
        
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
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
        \n1 success: release opponent GROUNDCONTROL or get GROUNDCONTROL or points\
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if defender.groundcontrol:
                defender.lose_groundcontrol() 
            elif attacker.groundcontrol:
                attacker.points += 1
            else:
                attacker.get_groundcontrol()       
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
                return(1)          
        return(0)
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
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
        \nchance for TAKEDOWN (~15%)"
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose",  "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("success", "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("success", "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
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
        return(sum(result))

    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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
        \n0 successes: reduce points, funny description"
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
        return(sum(result ))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
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
        return(sum(result ))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
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
        self.cost = 3
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
        return(sum(result ))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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
            defender.get_groundcontrol() 
            attacker.points -= 1
            

        
class Roar_Naked_Choke(Groundcards): 
    def __init__(self):
        self.name = "Roar naked choke"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction =["ground", "OP_NO_groundcontrol"]
        
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
            "lose"   : "Failed to control opponent, does he go for a leg?"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "roar naked choke"]}
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
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
                attacker.lose_groundcontrol() 
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
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
            elif effect == "loseground": attacker.lose_groundcontrol() 
            elif effect == "oground": defender.get_groundcontrol() 
            elif effect == "rpoints": attacker.points -= 1
            elif effect == "standup": attacker.currentfight.setStandup(True)
        elif maped_score == "lose":
            attacker.groundcontrol = False
            effect = choice(["standup", "ground"])
            if effect == "standup": attacker.currentfight.setStandup(True)
            elif effect == "ground": defender.get_groundcontrol() 
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
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
            attacker.lose_groundcontrol() 
            defender.get_groundcontrol() 
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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


class Devastating_Overhand(Standupcards):                                                                              ################################ HERE CONTINUE
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
        return(result.get(maped_score,["N/A", "N/A"]))      
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.muay_thai))
        return(sum(result ))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "win")
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.fightlost()  
        elif maped_score == "success":
            attacker.points += 1
            attacker.currentfight.setStandup(False)
            if choice(["lostposition", "no"]) == "lostposition":
                defender.get_groundcontrol()           
        elif maped_score == "defeat":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
            defender.get_groundcontrol() 
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 2
            attacker.currentfight.setStandup(False)
            attacker.get_groundcontrol() 
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
        self.restriction = []  # only for unusual cards
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win", "win")
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
            attacker.lose_groundcontrol() 
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
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.got_rocked()
            defender.lose_groundcontrol() 
            attacker.get_groundcontrol()
            attacker.points += 2     
        elif maped_score == "success":
            defender.groundcontrol = False
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.currentfight.setStandup(True)



class Single_Leg(Standupcards):
    def __init__(self):
        self.name = "Single leg"
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
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
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



class Trip_Kick(Standupcards):
    def __init__(self):
        self.name = "Trip kick"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: muay thai\neffects(1 roll):\
        \n1 success: TAKEDOWN"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Kick to the leg, opponents trips and fights goes to the ground",
            "success": "",
            "defeat" : "",
            "lose"   : "Kick and miss"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.currentfight.setStandup(False)
        elif maped_score == "success":
            pass 
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass
            


class Technical_Stand_Up(Groundcards): 
    def __init__(self):
        self.name = "Technical stand up"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction = ["ground", "OP_NO_groundcontrol"]
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent wrestling, boxing\neffects(2roll):\
        \n2 success: STANDUP\
        \n1 success: STANDUP if GROUNDCONTROL otherwise STANDUP(25% chance)\
        \n0 success: suffer DAMAGE, reduce points\
        CANNOT WORK IF OPPONENT HAS GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Technical stand up like one from the bjj manual",
            "success": "He is lifting his hips, he'll get back on feet, won't he?",
            "defeat" : "",
            "lose"   : "He tried to stand up but was countered"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"lose":["TKO", "punches(GnP)"]}
        return(result.get(maped_score,["N/A", "N/A"]))  
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.bjj, defender.boxing))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose",  "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.currentfight.setStandup(True)    
        elif maped_score == "success":
            if attacker.groundcontrol:
                attacker.currentfight.setStandup(True)
            else: 
                if choice(["standup", "no", "no", "no"]) == "standup":
                    attacker.currentfight.setStandup(True)
        elif maped_score == "defeat":
            pass 
        elif maped_score == "lose":
            attacker.got_hurt()
            attacker.points -= 1
  
  

class Front_Kick(Standupcards):
    def __init__(self):
        self.name = "Front kick"
        self.rarity = "uncommon"
        self.quantity = 2
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: muay thai\neffects(2 roll):\
        \n2 success: apply DAMAGE, points\
        \n1 success: TIMELAPSE\
        \n<skillcard designed by Kamil J>"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "The suprise kick causes some damage!",
            "success": "The opponent is pushed back",
            "defeat" : "",
            "lose"   : "The foot swings in the air..."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "Kick"]}
        return(result.get(maped_score,["N/A", "N/A"])) 
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.muay_thai))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 1
            defender.got_hurt()
        elif maped_score == "success":
            attacker.currentfight.moveTimer()  
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass



class Triangle_Choke(Groundcards):  
    def __init__(self):
        self.name = "Triangle choke"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction = ["ground", "groundcontrol"]
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent bjj\neffects(2roll):\
        \n2 success: WIN the fight\
        \n1 success: apply DAMAGE, points\
        \n0 success: lose GROUNDCONTROL, reduce points, 50% for TIMELAPSE\
        \nCAN BE PLAYED ONLY IF YOU HAVE GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He catches the opponent in the perfect triangle. It's all over!",
            "success": "He has opponent in a triangle. Can he finish it?",
            "defeat" : "",
            "lose"   : "He tried something but the Opponent easily passed the legs."}
        return(results)
    
    def win_descriptions(self, maped_score):
        desc_success  = choice([["Submission", "Triangle"], \
                                ["Submission", "armlock from triangle"], ["TKO", "punches from triangle"]])
        result = {"win":["Submission", "Triangle"],
                  "success": desc_success
                  }
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):

        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.fightlost()
            attacker.points += 1
        elif maped_score == "success":
            defender.got_hurt()
            attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.lose_groundcontrol()
            defender.points += 1
            if randint("timelapse", "no") == "timelapse":             
                attacker.currentfight.moveTimer() 

 
class Leglock_Scramble(Groundcards):  
    def __init__(self):
        self.name = "Leglock scramble"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: bjj(3),wrestling(1)\neffects(4roll):\
        \n4,3 success: points, WIN if GROUNDCONTROl else GROUNDCONTROL\
        \n2 success: apply GROUNDCONTROL\
        \n1 success: reduce points\
        \n0 success: reduce points LOSE if op GROUNDCONTROL else op GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "The opponents leg is trapped!",
            "success": "He fakes a submission attempt and takes the dominant position.",
            "defeat" : "It looks like he is outgrappled by the opponent.",
            "lose"   : "The opponent wins the scramble on the ground and even threatens with a submission!"}
        return(results)
    
    def win_descriptions(self, maped_score):
        desc_win = choice([["Submission", "Leglock"], ["Submission", "Kneebar"], ["Submission", "Heel hook"]])
        result = {"win":desc_win,
                  "lose": desc_win
                  }
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if attacker.groundcontrol: defender.fightlost()
            else: attacker.get_groundcontrol()
            attacker.points += 1
        elif maped_score == "success":
            attacker.get_groundcontrol()
        elif maped_score == "defeat":
            attacker.points -= 1
        elif maped_score == "lose":
            attacker.points -= 1
            if defender.groundcontrol: attacker.fightlost()
            else: defender.get_groundcontrol()            
 
 
class Heel_Hook(Groundcards):  
    def __init__(self):
        self.name = "Heel hook"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: bjj\neffects(3roll):\
        \n3 success: you WIN\
        \n2 success: points\
        \n1,0 success: reduce points, lose GROUNDCONTROL, op GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "And here is the tapout! He takes opponent leg home with him tonight! What a nasty heel hook",
            "success": "He controls the opponent's knee, it looks like it's all over... No, the opponent has released his leg somehow.",
            "defeat" : "You can call that one a HELL hook as after the attempt he's in real trouble.",
            "lose"   : "The bravado didn't pay off. After a reverse the opponent is in the dominant position."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "Heel hook"]}
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(3):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.fightlost()
        elif maped_score == "success":
            attacker.points += 1
        elif maped_score == "defeat":
            attacker.points -= 1
            defender.get_groundcontrol()
            attacker.lose_groundcontrol()
        elif maped_score == "lose":
            attacker.points -= 1
            defender.get_groundcontrol()
            attacker.lose_groundcontrol()
            
            

class Suplex(Standupcards):
    def __init__(self):
        self.name = "Suplex"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 4
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your wrestling, opponent wrestling, 4 rolls\neffects:\
        \n4 success: TAKEDOWN, apply ROCKED, GROUNDCONTROL, points*2\
        \n3 success: TAKEDOWN, apply DAMAGE, points\
        \n0 successes: TAKEDOWN, reduce points, op GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He lifts the opponent and slams him madly into the mat. His head connected first... Hopefully no injury here!",
            "success": "He tries a suplex and he gets it! What a throw. Unbeliviable!",
            "defeat" : "The opponent is resisting the throws attempts",
            "lose"   : "He tried a high throw but he was countered"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "Slam (from suplex)"],
                 "success" :["TKO", "Slam and punches"],
                  }
        return(result.get(maped_score,["N/A", "N/A"]))        
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            defender.got_rocked()
            attacker.points += 2
            attacker.currentfight.setStandup(False)
            attacker.get_groundcontrol()
        elif maped_score == "success":
            defender.got_hurt()
            attacker.points += 1
            attacker.currentfight.setStandup(False)            
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
            attacker.currentfight.setStandup(False)
            defender.get_groundcontrol()   
            


class Knees_In_Clinch(Standupcards):
    def __init__(self):
        self.name = "Knees in clinch"
        self.rarity = "common"
        self.quantity = 1 
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: muaythai and wrestling, 4 rolls\neffects:\
        \n4 success: apply ROCKED, points\
        \n3 success: apply DAMAGE, points\
        \n0 successes: reduce points, TAKEDOWN"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Opponent's head is too low. He eats a knee... and another one!",
            "success": "Good knees here.",
            "defeat" : "Just clinchwork.",
            "lose"   : "The opponent takes the fight from the clinch into the ground."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "knee"],
                  "success":["TKO", "knee"]
                  }
        return(result.get(maped_score,["N/A", "N/A"])) 
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(4):
            result.append(attacker.roll_2_stat(attacker.muay_thai, attacker.wretling, defender.muay_thai, defender.wrestling))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points += 1
            defender.got_rocked()
        elif maped_score == "success":
            attacker.points += 1
            defender.got_hurt() 
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.currentfight.setStandup(False)
            attacker.points -= 1



class Sit_Out_Spin(Groundcards):
    def __init__(self):
        self.name = "Sit out spin"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction = ["ground", "NO_groundcontrol"]
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your wrestling, opponent wrestling,bjj \neffects(2roll):\
        \n2 success: apply GROUNDCONTROL, opponent lose GROUNDCONTROL, points\
        \n1 success: STANDUP\
        \n0 success: op gets GROUNDCONTROL, reduce points\
        CAN BE TRIGGER ONLY IF YOU DON'T HAVE GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "It comes out from under the opponent. He can take the back mount now.",
            "success": "He controls the opponents arm, spins out from under him, but he is pushed back.",
            "defeat" : "",
            "lose"   : "He tries the escape but is pinned down to the mat."}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.get_groundcontrol()
            defender.lose_groundcontrol()
            attacker.points += 1
        elif maped_score == "success":
            attacker.currentfight.setStandup(True)
        elif maped_score == "defeat":
            pass 
        elif maped_score == "lose":
            defender.get_groundcontrol()
            attacker.points -= 1
    


class Guillotine(Groundcards):
    def __init__(self):
        self.name = "Guillotine"
        self.rarity = "common"
        self.quantity = 1
        self.cost = 4
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction = []
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your wrestling, opponent wrestling,bjj \neffects(2roll):\
        \non the ground:\
        \n2 success: apply TIRED, points\
        \n1 success: 10% WIN the fight, if GROUNDCONTROL points\
        \n0 success: suffer TIRED, reduce points\
        \nin the standup:\
        \n2 success: (TAKEDOWN with GROUNDCONTROL) or DAMAGE, points\
        \n1 success: 50% for (TAKEDOWN with op GROUNDCONTROL and reduce points), 5% WIN the fight\
        \n0 success: reduce points\
        SKILL CAN BE USED ON THE GROUND AND IN THE STANDUP"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He applies tight front lock! The opponent is in serious troubles!",
            "success": "Will he submit the opponent with a guillotine? I don't think so, but who knows...",
            "defeat" : "",
            "lose"   : "He failed to control the opponents head. It took a lot of gas from him."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "guillotine"],
                  "success":["Submission", "guillotine"],
                  "lose" : ["TKO", "punches (GnP)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))     
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.wrestling))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 1
            if self.standup:
                if choice("ground", "no") == "ground":
                    attacker.currentfight.setStandup(False)
                    attacker.get_groundcontrol()
                else:defender.got_hurt()
            else: defender.got_tired()
        elif maped_score == "success":
            if self.standup:
                if randint(1, 20) == 20: defender.lost = True
                if choice("ground", "no") == "ground":
                    attacker.currentfight.setStandup(False)
                    defender.get_groundcontrol()
                    attacker.points -= 1
            else:
                if randint(1, 10) == 10: defender.lost = True
                if attacker.groundcontrol: attacker.points += 1
        elif maped_score == "defeat":
            pass 
        elif maped_score == "lose":
            attacker.points -= 1
            if self.standup:pass
            else: attacker.got_tired()            

     

class Bjj_Shrimp(Groundcards):
    def __init__(self):
        self.name = "Bjj shrimp"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 0
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction = ["ground", "OP_groundcontrol"]
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent bjj\neffects(1roll):\
        \n1 success: opponent lose GROUNDCONTROL\
        ONLY IF THE OPPONENT HAS GROUNDCONTROL"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "What a great escape!",
            "success": "",
            "defeat" : "",
            "lose"   : "He is shrimping but with no success"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.lose_groundcontrol() 
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass


 
class Crucifix(Groundcards):
    def __init__(self):
        self.name = "Crucifix"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, opponent bjj\neffects(2roll):\
        \n2 success: apply GROUNDCONTROL, points, if already: apply DAMAGE\
        \n1 success: apply GROUNDCONTROL, if already: points\
        \n0 success: op gets GROUNDCONTROL, if already: reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "The opponent is caught in crucifix. The question is: he'll be submitted or maybe KO'ed?",
            "success": "The opponent is caught in crucifix.",
            "defeat" : "",
            "lose"   : "Looks like he is giving the position to the opponent..."}
        return(results)
    
    def win_descriptions(self, maped_score):
        type_method = choice([["Submission", "neck crank"], ["TKO", "punches (GnP from crucifix)"]])
        result = {"win": type_method}
        return(result.get(maped_score,["N/A", "N/A"]))   
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 1
            if attacker.groundcontrol: defender.got_hurt()
            else: attacker.get_groundcontrol()       
        elif maped_score == "success":        
            if attacker.groundcontrol: attacker.points += 1
            else: attacker.get_groundcontrol()
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            if defender.groundcontrol: attacker.points -= 1
            else: defender.get_groundcontrol() 
 


class Hammerfists(Groundcards):
    def __init__(self):
        self.name = "Hammerfists"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your boxing(2), wrestling(1), opponent bjj\neffects(2roll):\
        \n2 success: apply ROCKED if GROUNDCONTROL, otherwise DAMAGE, points*2\
        \n1 success: apply DAMAGE if GROUNDCONTROL, points\
        \n0 success: lose GROUNDCONTROL, opponent GROUNDCONTROL, reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He's hammering his opponent head... What a beating! Where is refree?",
            "success": "These hammerfists can leave a bruise",
            "defeat" : "",
            "lose"   : "He tried ground and pound and got swept"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win": ["TKO", "punches (GnP)"],
                  "success" : ["TKO", "punches (GnP)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))   
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
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
            pass 
        elif maped_score == "lose":
            attacker.lose_groundcontrol() 
            defender.get_groundcontrol() 
            attacker.points -= 1


class GnP_Elbows(Groundcards): 
    def __init__(self):
        self.name = "GnP elbows"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 3
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your muaythai(3),wrestling(1)  opponent bjj\neffects(4roll):\
        \n4 success: apply ROCKED and DAMAGE if GROUNDCONTROL, otherwise DAMAGE*2, points*2\
        \n3 success: apply DAMAGE*2 if GROUNDCONTROL, otherwise DAMAGE, points\
        \n0 success: lose GROUNDCONTROL, opponent GROUNDCONTROL, reduce points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "The opponent's face is covered with blood. That one should be over in no time.",
            "success": "He's raining elbows from the top and looking for a finish!",
            "defeat" : "Few insignificant elbow punches won't do the job.",
            "lose"   : "Never play on the ground with bjj shark or you'll get swept like this!"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["TKO", "elbows(GnP)"],
                  "success":["TKO", "elbows(GnP)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))  
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.bjj))
            result.append(attacker.roll_1_stat(attacker.wrestling, defender.bjj))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if attacker.groundcontrol:
                defender.got_rocked()
                defender.got_hurt()
            else: 
                defender.got_hurt()
                defender.got_hurt()
            attacker.points += 2     
        elif maped_score == "success":
            if attacker.groundcontrol:
                defender.got_hurt()
            defender.got_hurt()
            attacker.points += 1 
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.lose_groundcontrol() 
            defender.get_groundcontrol() 
            attacker.points -= 1
            


class Uppercut(Standupcards):
    def __init__(self):
        self.name = "Uppercut"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 1
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: boxing\neffects(2 roll):\
        \n2 success: apply ROCKED, points"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Perfectly timed uppercut lands on the opponents chin!",
            "success": "",
            "defeat" : "Hit and miss.",
            "lose"   : "Uppercut blocked."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "uppercut"]}
        return(result.get(maped_score,["N/A", "N/A"]))   
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "defeat", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 1
            defender.got_rocked()
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass  



class Drunkenjitsu(Groundcards):
    def __init__(self):
        self.name = "Drunkenjitsu"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        self.restriction = ["ground", "tired"]
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: bjj,wrestling \neffects(2roll):\
        \n2 success: WIN if op TIRED else apply GROUNDCONTROL and DAMAGE\
        \n1 success: WIN if op TIRED else apply GROUNDCONTROL\
        \n0 success: apply DAMAGE, suffer DAMAGE\
        SKILL TRIGGERS ONLY IF YOU ARE TIRED"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "That moves are out of the box, but... Bite him!",
            "success": "He is appling some kind of odd hold. Or maybe he wants to kiss the opponent...",
            "defeat" : "",
            "lose"   : "It does look to me like these fighters aren't exactly 100% sober. Or maybe I have to drink"}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["Submission", "punches (GnP)"],
                  "win":["Submission", "choke"],
                  "lose":["TKO", "punches (GnP)"]
                  }
        return(result.get(maped_score,["N/A", "N/A"])) 
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(2):
            result.append(attacker.roll_2_stat(attacker.bjj, attacker.wrestling, defender.bjj, defender.wrestling))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            if defender.weak: defender.lost == True
            else: 
                attacker.get_groundcontrol()
                defender.got_hurt()
        elif maped_score == "success":        
            if defender.weak: defender.lost == True
            else: 
                attacker.get_groundcontrol()
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.got_hurt()
            defender.got_hurt()

 
 
class Superman_Punch(Standupcards):
    def __init__(self):
        self.name = "Superman punch"
        self.rarity = "rare"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your boxing(3),muaythai(2), op boxing\neffects(5 roll):\
        \n5 success: apply ROCKED,DAMAGE, points*3\
        \n4 success: apply DAMAGE points*2\
        \n3 success: lowers op box,mt by 2, points\
        \n2-0 success: random: TAKEDOWN, red.points, DAMAGE, no effect\
        "
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "Holy Molly.This Superman punch was legendary!",
            "success": "Flying cross right on the chin!",
            "defeat" : "He feigns a kick and punch! The opponent is totally confused!",
            "lose"   : "He tried Superman punch, but it was not even a Batman slap. And he eats one."}
        return(results)
    
    def win_descriptions(self, maped_score):
        result = {"win":["KO", "superman punch"],
                  "win":["TKO", "superman punch"],
                  "lose":["TKO", "punch"]
                  }
        return(result.get(maped_score,["N/A", "N/A"]))   
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.muay_thai, defender.boxing))
            result.append(attacker.roll_1_stat(attacker.boxing, defender.boxing))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "lose", "lose", "defeat", "success", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            attacker.points += 3
            defender.got_rocked()
            defender.got_hurt()
        elif maped_score == "success":
            attacker.points += 2
            defender.got_hurt()
        elif maped_score == "defeat":
            attacker.points += 1
            defender.boxing -= 2
            defender.muay_thai -= 2
        elif maped_score == "lose":
            roll = choice("no", "ground", "damage", "points") 
            if roll == "ground":
                attacker.currentfight.setStandup(False)
            elif roll == "damage":
                attacker.got_hurt()
            elif roll == "points":
                attacker.points -= 1
  
 
 
class Footwork(Standupcards):
    def __init__(self):
        self.name = "Footwork"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your boxing, op muaythai   \neffects(1 roll):\
        \n1 success: opponenent boxing and muaythai reduced by 2"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He totally controls the pace of the fight! Give him 5 minutes and we will see a knockout",
            "success": "",
            "defeat" : "",
            "lose"   : "He is trying to control the distance but the opponent is contantly breaking the habit"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.boxing, defender.muay_thai))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.boxing -= 2
            defender.muay_thai -= 2            
        elif maped_score == "success":
            pass
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            pass
  

 
class Grappling_Tricks(Groundcards):
    def __init__(self):
        self.name = "Grappling tricks"
        self.rarity = "uncommon"
        self.quantity = 1
        self.cost = 2
        self.description = self.description()
        self.results = self.all_results()
        self.result_description = ""
        
    def description(self):
        result = Skillcards.get_basedescription(self.name, self.rarity, self.quantity, self.cost) +"\
        \ntests: your bjj, op wrestling  \neffects(1 roll):\
        \n1 success: opponenent bjj and wrestling reduced by 2"
        return(result)
    
    def all_results(self):
        results ={
            "win"    : "He totally outgrappled his opponent! He can trick the opponent and go for a submission in any moment!",
            "success": "",
            "defeat" : "",
            "lose"   : "The opponent shows decent defence on the ground. He refuses to get caught in that technical game"}
        return(results)
    
    def roll_attack(self, attacker, defender):
        result = []
        for _ in range(1):
            result.append(attacker.roll_1_stat(attacker.bjj, defender.wrestling))
        return(sum(result))
    
    def get_attack_result(self, score):
        mapping = ("lose", "win")
        return(mapping[score])
        
    def attack_effect(self, maped_score, attacker, defender):  
        if maped_score == "win":
            defender.bjj -= 2
            defender.wrestling-= 2            
        elif maped_score == "success":
            pass
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

#killer kick
#butthead
#superman punch

#Kata-guruma
#Sweep_trip_throw
#throw directly to the groundcontrol

#mount position --> groundcontrol/punch

#muaythai GNP
#Escape!
#cheap shots --> points on the ground
#vicous hammerfist
#drunkenjitsu --> ground action better when tired
#reverse?