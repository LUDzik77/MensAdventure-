#MAIN FIGHT ENGINE
from random import randint, choice
import fighters_template
import Skillcards_map_and_create as Sk_create
from Skillist_with_weights import all_skills_equal_weights
import uuid
import logging
formatter1 = logging.Formatter('%(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')


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
        # fighter with groundcontrol can KO/submit easier, this attribute have to be set >False after every standup
        self.groundcontrol = False  
        self.skilllist = skilllist # quantity for a skills is generated as an attribute "quantity"
        self.secret_move = (choice(all_skills_equal_weights)[0],1)
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
            self.energy = 1
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
            
    def get_groundcontrol(self):
        if self.groundcontrol == True: pass
        else: 
            self.groundcontrol = True
            self.currentfight.prompt_fight_info(" has a groundcontrol now!", player=self.fullname)
            
    def lose_groundcontrol(self):
        if self.groundcontrol == False: pass
        else: 
            self.groundcontrol = False
            self.currentfight.prompt_fight_info(" lose groundcontrol", player=self.fullname)    
        
    def roll_1_stat(self, own_stat, op_stat):
        own_stat = own_stat if own_stat>0 else 1
        op_stat = op_stat if op_stat>0 else 1
        roll_your = randint(0, own_stat)
        roll_op = randint(0, op_stat)
        result = roll_your>=roll_op
        return(result)
        
    def roll_2_stat(self, own_stat1, own_stat2, op_stat1, op_stat2):
        own_stat1 = own_stat1 if own_stat1>0 else 1
        op_stat1 = op_stat1 if op_stat1>0 else 1
        own_stat2 = own_stat2 if own_stat2>0 else 1
        op_stat2 = op_stat2 if op_stat2>0 else 1
        a=self.roll_1_stat(own_stat1, op_stat1)
        b=self.roll_1_stat(own_stat1, op_stat2)
        c=self.roll_1_stat(own_stat2, op_stat1)
        d=self.roll_1_stat(own_stat2, op_stat2)
        if sum([a,b,c,d])>=2:
            result=True
        elif sum([a,b,c,d])<2:
            result=False
        else:
            result = randint(0,9)>4
        return(result)
    
    def fightlost(self):  
        self.lost = True
        
    def update_possible_victory_details(self, victorytype, victorymethod):
        self.victoryinfo_if_win = [victorytype, victorymethod]


class Match:
    def __init__(self, fighter1, fighter2, fight_time):
        self.match_hex_id = uuid.uuid4().hex
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.activeplayer = choice([self.fighter1, self.fighter2])
        self.inactiveplayer = self.fighter1 if self.activeplayer == self.fighter2 else self.fighter2
        self.fight_time = fight_time
        self.fight_is_not_over = True
        self.standup = True
        self.timer = 0
        self.inactivity_level = 0 # we will use this flague to switch to standup/ground if no action
        self.matchresult= ["victorytype", "victorymethod"]
        self.winner = ""
        self.initialize_logs()
        self.log_in_initialisation()

    def setup_logger(self, name, formatter, log_file, level=logging.INFO):
        handler = logging.FileHandler(log_file)        
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler) 
        return logger
    
    def initialize_logs(self):
        single_fights_logger_filename =  "".join((
            "fightgame_logs/single_fights/", self.fighter1.lastname, self.fighter2.lastname, "_ID_=", self.match_hex_id, ".log"))
        self.single_fight_logger = self.setup_logger(
            'single_fights_logger', formatter1, single_fights_logger_filename)
        self.fightgame_logger = self.setup_logger(
            'fightgame_logger', formatter2, "fightgame_logs/fightgamelog.log")
        
    def log_in_initialisation(self):
        self.fightgame_logger.info(f"MATCH_HEX_ID = {self.match_hex_id}\n")
        self.fightgame_logger.info(f"{self.activeplayer}, {self.inactiveplayer}")


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
            self.check_if_match_ended_early()
            if self.fight_time < self.timer:
                self.decision_victory()
                self.fight_is_not_over=False
            self.end_round_remove_action()
            self.end_round_change_players()
    
    def end_round_change_players(self):
        self.activeplayer,self.inactiveplayer = self.inactiveplayer,self.activeplayer
        self.inactiveplayer.energy += 1
    
    def end_round_remove_action(self):
        #print(len(self.activeplayer.skilllist), len(self.inactiveplayer.skilllist))
        self.activeplayer.skilllist = [x for x in self.activeplayer.skilllist if x.quantity>0]
        self.inactiveplayer.skilllist = [x for x in self.inactiveplayer.skilllist if x.quantity>0]
        #print(len(self.activeplayer.skilllist), len(self.inactiveplayer.skilllist))

    def check_if_match_ended_early(self):
        if sum([fighter1.lost,fighter2.lost]) == 1: 
            self.nondecision_victory()
    
    def end_match(self):                                            
        self.prompt_fight_info("END OF THE FIGHT")
        self.prompt_fight_info(f"{self.winner.fullname if self.winner is not None else 'No victor'}{self.matchresult}")
        self.fight_is_not_over = False
        
    def get_victor_decision(self):
        if self.fighter1.points > self.fighter2.points: self.winner = self.fighter1
        elif self.fighter2.points > self.fighter1.points: self.winner = self.fighter2
        else: self.winner = None         
        
    def get_victor_nondecision(self):
        if self.fighter1.lost: self.winner = self.fighter2
        elif self.fighter2.lost: self.winner = self.fighter1
        else: print("error in getting victor object <get_victor_nondecision>")
            
    def decision_victory(self):
        self.get_victor_decision()
        if self.fighter1.points-self.fighter2.points==0:
            victorymethod = choice(["Unanimous", "Split", "Majority"])
            self.matchresult =  ["Draw", victorymethod]       
        elif self.fighter1.points+1 == self.fighter2.points or \
             self.fighter2.points+1 == self.fighter1.points:
            victorymethod = choice(["Split", "Split", "Majority"])
            self.matchresult =  ["Decision", victorymethod]
        else:
            self.matchresult =  ["Decision", "Unanimous"]
        self.end_match()

    def nondecision_victory(self):
        self.get_victor_nondecision()
        self.matchresult = self.activeplayer.victoryinfo_if_win
        self.end_match()
    
    def start_round(self):
        self.moveTimer()
        self.check_if_standup_or_ground_changed()
        self.check_secret_move_addition()
        action = self.get_skill_to_use_in_attack()
        if action == None:
            self.inactivity_level+=1
            self.prompt_fight_info("is doing totally nothing", player=self.active_fullname())
        elif self.activeplayer.weak and randint(1,3)==3:
            self.prompt_fight_info("is taking a big breath", player=self.active_fullname())
            self.inactivity_level+=1
            self.activeplayer.energy += 2
        else:
            self.use_skill(action)
            self.activeplayer.energy-=action.cost
            action.quantity -= 1
    
    def check_secret_move_addition(self):
        if len(self.activeplayer.skilllist)<3 and randint(1,3) == 1:
            self.activeplayer.skilllist.append(Sk_create.get_1_Skillcard_object(self.activeplayer.secret_move))
            self.prompt_fight_info("has a secret technique on his disposal...", player=self.activeplayer.lastname)
            #print(f"<<<<<<<<<<<<<<<<<<SECRET MOVE ADDED>>>>>>>>>>>>>> {self.activeplayer.skilllist[-1].name}")
        
    #prompt will be passed to RenPy for render
    def prompt_fight_info(self, info, *args, **kwargs):
        p1 = self.active_fullname()
        if "action" in kwargs:
            print(f"{p1} <{kwargs['action']}>:\n{info}\n")
            self.single_fight_logger.info(f"{p1} <{kwargs['action']}>:\n{info}\n")
        elif "player" in kwargs:
            print(f"{kwargs['player']} {info}\n")
            self.single_fight_logger.info(f"{kwargs['player']} {info}\n")
        else:
            print(f"{info}\n")
            self.single_fight_logger.info(f"{info}\n")

    def check_if_standup_or_ground_changed(self):
        if self.inactivity_level > 8:self.inactivity_level=8 
        if randint(1, 10-self.inactivity_level)== 1:
            self.changeStandup()
            
    def get_skill_to_use_in_attack(self):
        legal_actions = self.get_pool_of_possible_attacks()
        #return(None if len(legal_actions)== 0 else choice(legal_actions))
        energy_legal_actions = self.get_pool_of_energy_legal_attacks(legal_actions)
        return(None if len(list(energy_legal_actions))== 0 else choice(list(energy_legal_actions)))
    
    def get_pool_of_possible_attacks(self):                                    
        not_restricted = []
        for skill in self.activeplayer.skilllist:
            skill_allowed = True
            for restriction in skill.restriction:
                if restriction == "standup" and self.standup==False: skill_allowed=False
                elif restriction == "ground" and self.standup: skill_allowed=False
                elif restriction == "groundcontrol" and self.activeplayer.groundcontrol==False: skill_allowed=False
                elif restriction == "OP_groundcontrol" and self.inactiveplayer.groundcontrol==False: skill_allowed=False
                elif restriction == "NO_groundcontrol" and self.activeplayer.groundcontrol: skill_allowed=False
                elif restriction == "OP_NO_groundcontrol" and self.inactiveplayer.groundcontrol: skill_allowed=False
                elif restriction == "NO_groundcontrol" and self.activeplayer.groundcontrol: skill_allowed=False
                elif restriction == "tired" and self.activeplayer.weak==False: skill_allowed=False
                elif restriction == "rocked" and self.activeplayer.rocked==False: skill_allowed=False
                elif restriction == "OP_rocked" and self.inactiveplayer.rocked==False: skill_allowed=False
            if skill_allowed:
                not_restricted.append(skill)
        return(not_restricted)   
    
    def get_pool_of_energy_legal_attacks(self, legal_actions):
        print(self.activeplayer.fullname, self.activeplayer.energy)
        result = list(filter(lambda x:x.cost<=self.activeplayer.energy, legal_actions))
        print([(x.name, x.quantity) for x in result])
        if len(legal_actions) != len(result): print("at least 1 skill too costy")
        return(result)
      
    def use_skill(self, action, *args, **kwargs):
        action.use(attacker=self.activeplayer, defender=self.inactiveplayer)
        
    def changeStandup(self):
        if self.standup == True:
            self.setStandup(False)
        else: self.setStandup(True)
        self.inactivity_level = 0
    
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

    
    
if __name__ == "__main__":
    fighter1 = Fighter(*fighters_template.Saladin_Tuahihi)
    fighter2 = Fighter(*fighters_template.Mr_test)
    The_Fight = Match(fighter1, fighter2, 12)
    fighter1.currentfight = The_Fight 
    fighter2.currentfight = The_Fight
    print(fighter1.firstname,[(x.name, x.quantity) for x in fighter1.skilllist])
    print(fighter2.firstname,[(x.name, x.quantity) for x in fighter2.skilllist])
    The_Fight.start_fight()
    #print("standup = ", The_Fight.standup)
    #print(fighter1.firstname, "T:",fighter1.weak,  "R:", fighter1.rocked, "L:", fighter1.lost, "points:", fighter1.points)
    #print(fighter2.firstname, "T:",fighter2.weak,  "R:", fighter2.rocked, "L:", fighter2.lost, "points:", fighter2.points)

