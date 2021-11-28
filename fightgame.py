# Here will be main engine of fighting
from random import randint

#fight start in standup
STANDUP=True

class Fighter:
    
    def __init__(self, name, nickname, boxing, muay_thai, wrestling, bjj, energy):
        self.name = name
        self.nickname = nickname
        self.boxing = boxing
        self.muay_thai = muay_thai
        self.wrestling = wrestling
        self.bjj = bjj
        self.energy = energy
        self.weak = False
        self.rocked = False
        self.lost = False
        self.skills = [] # list of tuples: object ex. jab and quantity of jabs
        self.points = 0 #  to get the result at the end of the fight
        
    def got_rocked(self):
        if self.rocked == False:
            self.rocked == True        
        else:
            if randint(0, 1) == 0: 
                self.lost = True   
                
    def got_tired(self):
        if self.weak == False:
            self.weak = True
        elif self.energy == False:
            self.rocked == True        
        else:
            if randint(0, 1) == 0: 
                self.lost = True
                
    def got_hurt(self):
        roll_a_die = randint(1,4)
        if roll_a_die == 2:
            self.health -= 2
        elif roll_a_die == 3:
            self.got_tired()
        elif roll_a_die == 4:
            self.got_rocked()
        
       
    def roll_1_stat(self, own_stat, op_stat):
        roll_your = randint(0, own_stat)
        roll_op = randint(0, op_stat)
        result = True if roll_your>roll_op else False
        return(result)
        
    def roll_2_stat(self, own_stat1, own_stat2, op_stat1, op_stat2):
        a=self.roll_1_stat(own_stat1, op_stat1)
        b=self.roll_1_stat(own_stat1, op_stat2)
        c=self.roll_1_stat(own_stat2, op_stat1)
        d=self.roll_1_stat(own_stat2, op_stat2)
        if sum([a,b,c,d])>2:
            result=True
        elif sum([a,b,c,d])<2:
            result=False
        else:
            result = True if randint(0, 9)>4 else False
        return(result)


class Skillcards:
    def get_description(self, key):
        return(self.results[key])
    def use(self, attacker, defender):  
        score = self.roll_attack(self, attacker, defender)
        maped_score = self.get_attack_result(score)
        self.attack_effect(maped_score, attacker, defender)
   
      
class Standupcards(Skillcards):
    self.standup = True


class Groundcards(Skillcards):
    self.standup = False

    
class SJab(Standupcards):
    def __init__(self):
        self.name = "Jab"
        self.standup = True
        self.cost = 0
        self.description = self.description()
        self.results = self.results() 
    def description(self):
        return("Jab/ncost:0/ntest boxing --> get points")
    def results(self):
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
        
    def attack_effect(maped_score, attacker, defender):
        if maped_score == "win":
            attacker.points += 1
            defender.got_hurt()
        elif maped_score == "success":
            attacker.points += 1
        elif maped_score == "defeat":
            pass
        elif maped_score == "lose":
            attacker.points -= 1
    
    
    
    
    
AA = Fighter("AA", "AAAA",5,5,5,5,5)
BB = Fighter("BB", "BBBB",5,5,5,5,5)
result_ = AA.roll_2_stat(AA.bjj, AA.wrestling, BB.bjj, BB.wrestling)

print(result_)

