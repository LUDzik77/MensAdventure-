#here we map skills from strings to objects

import Skillcards as Sk

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
    "Jab jab cross": Sk.Jab_Jab_Cross
}


def get_1_Skillcard_object(to_map):
    new_object = all_skills[to_map[0]]()
    new_object.quantity = to_map[1]
    return(new_object)   



#list of skills for sampling + rarity:
'''
("Jab",1),
("Lowkick",1),
("Pull guard",1),           UNC
("Bearhug takedown",1),
("1-2-kick combo",1),
("Powerjab",1),             UNC
("Lay and pray",1),
("Brute force sweep",1),
("Lucky punch",1),          RARE**
("Granite chin",1),         UNC
("Cardio king",1),
("Swing for the fences",1),
("Windmill style",1),
("Slap",1),
("Highkick",1),             UNC
("Flying knee"),            RARE**
("Roar naked choke",1),
("Armbar",1),
("Ground and pound"),
("Dirty boxing",1),         UNC
("Devastating overhand",1), UNC
("Elbows",1),               RARE**
("Flying armbar",1),        RARE**
("Double leg",1),
("Universal punch",1),      RARE**
("Slam",1),                 RARE**
("Single leg",1),           UNC
("Trip kick",1),            UNC
("Technical stand up",1),
("Front kick",1),           UNC
("Triangle choke",1),       UNC
("Leglock scramble",1),     UNC
("Heel hook",1),            UNC
("Suplex",1),               RARE**
("Knees in clinch",1),
("Sit out spin",1),         UNC
("Guillotine",1),
("Bjj shrimp",1),           UNC
("Crucifix",1),             RARE**
("Hammerfists",1),          RARE**
("GnP elbows",1),           UNC
("Uppercut",1),             UNC
("Drunkenjitsu",1),         RARE**
("Superman punch",1),       RARE**
("Footwork",1),             UNC
("Grappling tricks",1),     UNC
("Kata guruma",1) ,         RARE**
("Lure brawler",1),         RARE**
("Girly blows",1),
("Killer instinct",1)       UNC
("Jab jab cross",1)
'''