# Here will be main engine of fighting
from random import randint, choice
import Skillcards as Sk
import fighters_template


#when it reaches a number 12(?) fight goes for decision

#  BOTH have to be add with setters and getters to MATCH

class Fighter: 
    def __init__(self, firstname, lastname, nickname, boxing, muay_thai, wrestling, bjj, energy, skilllist):
        # self.currentfight changed on runtime; 
        # serves to communicate between SkillCards and The_Fight and to avoid circular importing error
        self.currentfight  = False 
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.fullname = firstname + " " + lastname
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
        self.victoryinfo_if_win = ["victorytype", "victorymethod"] 
        
    def got_rocked(self):
        if self.rocked == False:
            self.rocked = True
            self.currentfight.prompt_fight_info(" is rocked!", player=self.fullname)
        else:
            self.lost = True   
                
    def got_tired(self):
        if self.weak == False:
            self.weak = True
            self.currentfight.prompt_fight_info(" is exhausted!", player=self.fullname)
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
            self.energy -= 2
        elif roll_a_die == 3:
            self.got_tired()
        elif roll_a_die == 4:
            self.got_rocked()
            
    def gets_groundcontrol(self):
        if self.groundcontrol == True: pass
        else: 
            self.groundcontrol = True
            self.currentfight.prompt_fight_info(" has a groundcontrol now!", player=self.fullname)
        
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
    
    def fightlost(self):  #used mostly with submissions
        self.lost = True
        
    def update_possible_victory_details(self, victorytype, victorymethod):
        self.victoryinfo_if_win = [victorytype, victorymethod]


class Match:
    def __init__(self, fighter1, fighter2, fight_time):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.activeplayer = choice([self.fighter1, self.fighter2])
        self.inactiveplayer = self.fighter1 if self.activeplayer == self.fighter2 else self.fighter2
        self.fight_time = fight_time
        self.fight_is_not_over = True
        self.standup = True
        self.timer = 0
        self.matchresult= ["victorytype", "victorymethod"]
        self.winner = ""
        # IDEA 1.we fill it when one fighter get  flag "lost" 
        # then checks for DQ card etc
        # then final result (or reset of selt.matchresult) 
        
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
        while self.fight_is_not_over:
            self.start_round()
            if self.fight_time < self.timer: 
                self.fight_is_not_over=False
            self.check_if_match_ended()
            self.end_round()
        self.end_match()
    
    def end_round(self):
        if self.activeplayer == self.fighter1: 
            self.activeplayer = self.fighter2
            self.inactiveplayer =self.fighter1
        else: 
            self.activeplayer = self.fighter1
            self.inactiveplayer = self.fighter2
            
    def check_if_match_ended(self):
        #here additional check for that DQ card  nooo :/
        if sum([fighter1.lost,fighter2.lost]) == 1: 
            self.nondecision_victory()
    
    def end_match(self):
        self.decision_victory()                                                ############################## temporary solution
        self.prompt_fight_info("END OF THE FIGHT")
        self.prompt_fight_info(f"{self.winner.fullname if self.winner is not None else 'No victor'}{self.matchresult}")
        
    def decision_victory(self):                                                #################################### test it please
        if self.fighter1.points > self.fighter2.points: self.winner = self.fighter1
        elif self.fighter2.points > self.fighter1.points: self.winner = self.fighter2
        else: self.winner = None         
        
        if abs(sum([self.fighter1.points, self.fighter2.points])) == 0:
            victorymethod = choice(["Unanimous", "Split", "Majority"])
            self.matchresult =  ["Draw", victorymethod]
        elif abs(sum([self.fighter1.points, self.fighter2.points])) == 1:
            victorymethod = choice(["Split", "Split", "Majority"])
            self.matchresult =  ["Decision", victorymethod]
        else:
            self.matchresult =  ["Decision", "Unanimous"]

    
    def nondecision_victory(self):
        # .victoryinfo_if_win
        #["victorytype", "victorymethod"]        
        pass
    
    def start_round(self):
        self.moveTimer()
        self.check_if_standup_or_ground_changed()
        # we need to implement ENERGY COST of attacs, fatique, add more RESTRICTIONS, hidden skill ; 
        action = self.get_skill_to_use_in_attack()
        if action == None:
            self.prompt_fight_info(" is doing totally nothing", player=self.active_fullname())
        elif self.activeplayer.weak and randint(1,3)==3:
            self.prompt_fight_info(" is taking a big breath", player=self.active_fullname())
            self.activeplayer.energy += 2
        else:
            self.use_skill(action)                                                                  
            if action.quantity <2:
                del action
            else: action.quantity -= 1
    
    #prompt will be passed to RenPy for render
    def prompt_fight_info(self, info, *args, **kwargs):
        p1 = self.active_fullname()
        if "action" in kwargs:
            print(f"{p1} <{kwargs['action']}>:\n{info}\n")
        elif "player" in kwargs:
            print(f"{kwargs['player']} {info}\n") 
        else:
            print(f"{info}\n")

    def check_if_standup_or_ground_changed(self):
        randomnr = randint(1, 9)
        if randomnr == 9:
            self.changeStandup()
            
    def get_skill_to_use_in_attack(self):
        actions = self.get_pool_of_possible_attacks()
        return(None if len(actions)== 0 else choice(actions))
    
    def get_pool_of_possible_attacks(self):
        not_restricted = []
        for skill in self.activeplayer.skilllist:
            if self.standup and "standup" in skill.restriction:
                not_restricted.append(skill)
            elif not self.standup and "ground" in skill.restriction:
                not_restricted.append(skill)
        return(not_restricted)   
      
    def use_skill(self, action, *args, **kwargs):
        action.use(attacker=self.activeplayer, defender=self.inactiveplayer)
        
    def changeStandup(self):
        if self.standup == True:
            self.setStandup(False)
        else: self.setStandup(True)
    
    def setStandup(self, value):
        if self.standup==value:
            print(f"error: Standup cannot change from {self.standup} to {value}")
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
print("standup = ", The_Fight.standup)
print("T:",fighter1.weak,  "R:", fighter1.rocked, "L:", fighter1.lost)
print("T:",fighter2.weak,  "R:", fighter2.rocked, "L:", fighter2.lost)

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
