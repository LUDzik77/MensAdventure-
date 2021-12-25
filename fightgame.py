# Here will be main engine of fighting
from random import randint, choice
import Skillcards as Sk
import fighters_template

#fight start in standup
STANDUP=True
#when it reaches a number 12(?) fight goes for decision
TIMER = 0
#  BOTH have to be add with setters and getters to MATCH

class Fighter: 
    def __init__(self, firstname, lastname, nickname, boxing, muay_thai, wrestling, bjj, energy, skilllist):
        # self.currentfight changed on runtime; 
        # serves to communicate between SkillCards and The_Fight and to avoid circular importing error
        self.currentfight  = False 
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.boxing = boxing
        self.muay_thai = muay_thai
        self.wrestling = wrestling
        self.bjj = bjj
        self.energy = energy
        self.weak = False
        self.rocked = False
        self.lost = False
        # fighter with groundcontrol can KO/submit easier, we have to understad that this attribute have to be set to False after every standup
        self.groundcontrol = False  
        self.skilllist = skilllist # quantity for a skills is generated as an attribute "quantity"
        self.points = 0 #  to get the result at the end of the fight
        
    def got_rocked(self):
        if self.rocked == False:
            self.rocked = True
        else:
            self.lost = True   
                
    def got_tired(self):
        if self.weak == False:
            self.weak = True
        elif self.energy > 2:
            self.energy = 0
        elif self.rocked == False:
            self.rocked = True      
        else:
            if randint(0, 1) == 0: 
                self.lost = True
     
    def got_hurt(self):
        roll_a_die = randint(1, 4)
        if roll_a_die == 2:
            self.energy-= 2
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


class Match:
    def __init__(self, fighter1, fighter2, fight_time):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.activeplayer = choice([self.fighter1, self.fighter2])
        self.inactiveplayer = self.fighter1 if self.activeplayer == self.fighter2 else self.fighter2
        self.fight_time = fight_time
        self.fight_is_not_over = True
        # these attributes will replace global STANDUP & TIMER   ########################################to be implemented soon ####################################
        self.standup = True
        self.timer = 0         
        
    def active_fullname(self):
        return(self.activeplayer.firstname + " " +self.activeplayer.lastname)
    
    def inactive_fullname(self):
        return(self.inactiveplayer.firstname + " " +self.inactiveplayer.lastname)    
    
    def about_a_fight(self):
        p1 = self.active_fullname()
        p2 = self.inactive_fullname()
        self.prompt_fight_info(f"{p1} is facing {p2} today\
                    \nCan {self.activeplayer.nickname} defeat {self.inactiveplayer.nickname}?")
 
    def start_fight(self):
        self.about_a_fight()
        global TIMER
        while self.fight_is_not_over:
            self.start_round()
            if self.fight_time < TIMER: 
                self.fight_is_not_over=False
            self.end_round()
        self.end_match()
    
    def end_round(self):
        if self.activeplayer == self.fighter1: 
            self.activeplayer = self.fighter2
            self.inactiveplayer =self.fighter1
        else: 
            self.activeplayer = self.fighter1
            self.inactiveplayer = self.fighter2
        
    def end_match(self):
        self.prompt_fight_info("END OF THE FIGHT")
    
    def start_round(self):
        global TIMER
        TIMER += 1
        self.check_if_standup_or_ground_changed()
        action = self.get_skill_to_use_in_attack()
        # we need to implement --> FATIGUE; energy cost of attacs,
        # and borderline cases: empty action, 
        #no energy for cards (this one can go in <get_skill_to_use_in_attack>) etc
        self.use_skill(action)
        self.prompt_fight_info(action.get_result_description(), action=action.name)
        if action.quantity <2:
            del action
        else: action.quantity -= 1
    
    #prompt will be passed to RenPy for render
    def prompt_fight_info(self, info, *args, **kwargs):
        p1 = self.active_fullname()
        if not "action" in kwargs:
            print(f"{p1}: {info}\n")
        else: print(f"{p1} <{kwargs['action']}>:\n{info}\n")
    
    def check_if_standup_or_ground_changed(self):
        randomnr = randint(1, 9)
        if randomnr == 9:
            self.changeStandup()
            
    def get_skill_to_use_in_attack(self):
        actions = self.get_pool_of_possible_attacks()
        return(choice(actions))
    
    def get_pool_of_possible_attacks(self):
        #TO BE IMPLEMENTED
        return(self.activeplayer.skilllist)   
      
    def use_skill(self, action, *args, **kwargs):
        action.use(attacker=self.activeplayer, defender=self.inactiveplayer)
        
    def changeStandup(self):
        if self.standup == True:
            self.setStandup(False)
        else: self.setStandup(True)
    
    def setStandup(self, value):
        if self.standup==value:
            pass
        else:
            self.activeplayer.groundcontrol = False 
            self.inactiveplayer.groundcontrol = False 
            self.standup = value 
            position_ = "stand-up" if self.standup==True else "ground"
            self.prompt_fight_info(f"Fight moves to the {position_}!")
            
    def moveTimer(self):
        self.timer += 1
    

fighter1 = Fighter(*fighters_template.Saladin_Tuahihi)
fighter2 = Fighter(*fighters_template.Mr_test)
The_Fight = Match(fighter1, fighter2, 12)
fighter1.currentfight = The_Fight 
fighter2.currentfight = The_Fight
The_Fight.start_fight()
print(The_Fight.standup)



## TEST PURPOSES ONLY  (obsolete):   ##################################################################
#AA = Fighter(*fighters_template.Saladin_Tuahihi)
#BB = Fighter(*fighters_template.Saladin_Tuahihi)
#print(BB.skilllist)
#print(AA.skilllist)
#attack1 = Sk.Jab()
#attack2 = Sk.Lowkick()
#attack3 = Sk.One_Two_Kick_Combo()
#attack4 = Sk.One_Two_Kick_Combo()
#attack5 = Sk.One_Two_Kick_Combo()
##attack3 = Sk.Pullguard()
##attack4 = Sk.Bearhug_takedown()
##attack5 = Sk.One_Two_Kick_Combo()
#attack1.use(attacker=AA, defender=BB)
#attack2.use(attacker=AA, defender=BB)
#attack3.use(attacker=AA, defender=BB)
#attack4.use(attacker=AA, defender=BB)
#attack5.use(attacker=AA, defender=BB)

#print("T:",BB.weak,  "R:", BB.rocked, "L:", BB.lost)
#print(AA.points)
#print("")
#print("T:",AA.weak,  "R:", AA.rocked, "L:", AA.lost)
#print(BB.points)
#print("")
#print(attack1.description)
#print("")
#print(attack3.description)


#hidden skill --> to be implemented

#time to be implemented