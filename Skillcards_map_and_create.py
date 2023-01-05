#here we map skills from strings to objects
import Skillcards as Sk
#from fightgame import fightgame_logger

def map_to_objects(list_of_objects_to_map):
    fighter_skillcards = []
    for to_map in list_of_objects_to_map:
        fighter_skillcards.append(get_1_Skillcard_object(to_map))
    return(fighter_skillcards)

all_skills ={
    "Jab":Sk.Jab,
    "Lowkick":Sk.Lowkick,
    "Pull guard":Sk.Pullguard,
    "Bearhug takedown":Sk.Bearhug_Takedown,
    "1-2-kick combo":Sk.One_Two_Kick_Combo,
    "Powerjab":Sk.Powerjab,
    "Lay and pray":Sk.Lay_And_Pray,
    "Brute force sweep":Sk.Brute_Force_Sweep,
    "Roar naked choke":Sk.Roar_Naked_Choke,
    "Lucky punch":Sk.Lucky_Punch,
    "Granite chin":Sk.Granite_Chin,
    "Cardio king":Sk.Cardio_King,
    "Swing for the fences":Sk.Swing_For_The_Fences,
    "Slap":Sk.Slap,
    "Highkick":Sk.Highkick,
    "Flying knee":Sk.Flying_Knee,
    "Armbar":Sk.Armbar,
    "Ground and pound":Sk.Ground_and_Pound,
    "Dirty boxing":Sk.Dirty_Boxing,
    "Devastating overhand":Sk.Devastating_Overhand,
    "Elbows":Sk.Elbows,
    "Windmill style":Sk.Windmill_Style,
    "Flying armbar":Sk.Flying_Armbar,
    "Double leg":Sk.Double_Leg,
    "Universal punch":Sk.Universal_Punch,
    "Slam":Sk.Slam,
    "Single leg":Sk.Single_Leg,
    "Trip kick":Sk.Trip_Kick,
    "Technical stand up":Sk.Technical_Stand_Up,
    "Front kick":Sk.Front_Kick, 
    "Triangle choke":Sk.Triangle_Choke,
    "Leglock scramble":Sk.Leglock_Scramble,
    "Heel hook":Sk.Heel_Hook,
    "Suplex": Sk.Suplex,     
    "Knees in clinch":Sk.Knees_In_Clinch,
    "Sit out spin":Sk.Sit_Out_Spin,       
    "Guillotine":Sk.Guillotine,
    "Bjj shrimp":Sk.Bjj_Shrimp,
    "Crucifix":Sk.Crucifix,
    "Hammerfists":Sk.Hammerfists,
    "GnP elbows":Sk.GnP_Elbows,   
    "Uppercut":Sk.Uppercut,  
    "Drunkenjitsu":Sk.Drunkenjitsu,
    "Superman punch":Sk.Superman_Punch,
    "Footwork":Sk.Footwork,  
    "Grappling tricks":Sk.Grappling_Tricks,
    "Kata guruma": Sk.Kata_Guruma,
    "Lure brawler": Sk.Lure_Brawler,
    "Girly blows": Sk.Girly_Blows,
    "Killer instinct": Sk.Killer_Instinct,
    "Jab jab cross": Sk.Jab_Jab_Cross,
    "Mount position": Sk.Mount_Position,
    "Sprawl": Sk.Sprawl,
    "Losing Move": Sk.Losing_Move
}


def get_1_Skillcard_object(to_map):
    new_object = all_skills[to_map[0]]()
    new_object.quantity = to_map[1]
    return(new_object)   



#list of skills for sampling + rarity:
'''
("Jab",4),
("Lowkick",4),
("Pull guard",4),           UNC
("Bearhug takedown",4),
("1-2-kick combo",4),
("Powerjab",4),             UNC
("Lay and pray",4),
("Brute force sweep",4),
("Lucky punch",4),          RARE**
("Granite chin",4),         UNC
("Cardio king",4),
("Swing for the fences",4),
("Windmill style",4),
("Slap",4),
("Highkick",4),             UNC
("Flying knee",4),          RARE**
("Roar naked choke",4),
("Armbar",4),
("Ground and pound",4),
("Dirty boxing",4),         UNC
("Devastating overhand",4), UNC
("Elbows",4),               RARE**
("Flying armbar",4),        RARE**
("Double leg",4),
("Universal punch",4),      RARE**
("Slam",4),                 RARE**
("Single leg",4),           UNC
("Trip kick",4),            UNC
("Technical stand up",4),
("Front kick",4),           UNC
("Triangle choke",4),       UNC
("Leglock scramble",4),     UNC
("Heel hook",4),            UNC
("Suplex",4),               RARE**
("Knees in clinch",4),
("Sit out spin",4),         UNC
("Guillotine",4),
("Bjj shrimp",4),           UNC
("Crucifix",4),             RARE**
("Hammerfists",4),          RARE**
("GnP elbows",4),           UNC
("Uppercut",4),             UNC
("Drunkenjitsu",4),         RARE**
("Superman punch",4),       RARE**
("Footwork",4),             UNC
("Grappling tricks",4),     UNC
("Kata guruma",4) ,         RARE**
("Lure brawler",4),         RARE**
("Girly blows",4),
("Killer instinct",4),       UNC
("Jab jab cross",4),
("Mount_Position",4),
("Sprawl",4),
("Losing Move",4)           NAJMAN-RARE
'''