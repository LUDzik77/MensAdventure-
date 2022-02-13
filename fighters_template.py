from random import choices
import Skillcards_map_and_create as Sk_create


def get_fightSkills(skillset_to_pick_from):
    string_list = choices([s[0] for s in skillset_to_pick_from], 
                          weights=[s[1] for s in skillset_to_pick_from], k=6)
    result =  list({i:string_list.count(i) for i in string_list}.items())
    return(result)

#ABOUT THOSE LISTS:
# list of skill with weights from which we random pick skillset (6) to fight
# TODO: a lot of lists to organise prepare the skillcards for type of fighters: drunken, wrestler, un-orthodox, grappler etc
All_skills_equal_weights = [
    ("Jab",1),
    ("Lowkick",1),
    ("Pull guard",1),
    ("Bearhug takedown",1),
    ("1-2-kick combo",1),
    ("Powerjab",1),
    ("Lay and pray",1),
    ("Brute force sweep",1),
    ("Roar naked choke",1),
    ("Lucky punch",1),
    ("Granite chin",1),
    ("Cardio king",1),
    ("Swing for the fences",1),
    ("Slap",1),
    ("Highkick",1),
    ("Flying knee",1),
    ("Armbar",1),
    ("Ground and pound",1),
    ("Dirty boxing",1),
    ("Devastating overhand",1),
    ("Elbows",1),
    ("Windmill style",1),
    ("Flying armbar",1),
    ("Double leg",1),
    ("Universal punch",1),
    ("Slam",1),
    ("Single leg",1),
    ("Trip kick",1),
    ("Technical stand up",1),
    ("Front kick",1), 
    ("Triangle choke",1),
    ("Leglock scramble",1),
    ("Heel hook",1),
    ("Suplex",1),     
    ("Knees in clinch",1),
    ("Sit out spin",1),       
    ("Guillotine",1),
    ("Bjj shrimp",1),
    ("Crucifix",1),
    ("Hammerfists",1),
    ("GnP elbows",1),   
    ("Uppercut",1),  
    ("Drunkenjitsu",1),
    ("Superman punch",1),
    ("Footwork",1),  
    ("Grappling tricks",1),
    ("Kata guruma",1),
    ("Lure brawler",1)
]


Some_common_skills = [
    ("Jab",1), ("Double leg",1), ("Ground and pound",1)
    ]

Saladin_Tuahihi =[
"Saladin", #firstname
"Tuahihi", #lastname
"The bun",#nickname
5,#boxing
5,#muay_thai
5,#wrestling
5,#bjj
8, #energy
Sk_create.map_to_objects(get_fightSkills(All_skills_equal_weights))
]

# TEST SK CREATION
#skill_obj_list = Sk_create.map_to_objects(Saladin_Tuahihi[8])
#for skill in skill_obj_list:
    #print(skill.name, skill.quantity)


Mr_test =[
"Mr Test", #firstname
"Tester", #lastname
"Test-o-steron",#nickname
5,#boxing
5,#muay_thai
5,#wrestling
5,#bjj
8, #energy
Sk_create.map_to_objects(get_fightSkills(All_skills_equal_weights))
]

#[print(x.name) for x in Mr_test[8]]



#The_Player =[
#"Kamilion", #firstname
#"Firry", #lastname
#"Lion",#nickname
#p_boxing,
#p_muay_thai,
#p_wrestling,
#p_bjj,
#fight_energy,  # to be implemented
#fight_skills # to be implemented
#]
##persistent.boxing,
##persistent.muay_thai,
##persistent.wrestling,
##persistent.bjj,


