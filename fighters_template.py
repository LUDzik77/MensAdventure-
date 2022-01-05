from random import choices
import Skillcards_map_and_create as Sk_create

def get_fightSkills(skillset_to_pick_from):
    string_list = choices([s[0] for s in skillset_to_pick_from], 
                          weights=[s[1] for s in skillset_to_pick_from], k=6)
    result =  list({i:string_list.count(i) for i in string_list}.items())
    return(result)

# list of skill with weights from which we random pick skillset (6) to fight
# do we randomize boxing, bjj skills as well?
Saladin_Tuahihi_skills = [("Lowkick", 1), ("Devastating overhand", 10), ("Powerjab", 5), ("Bearhug takedown", 10000),\
                                ("Brute force sweep", 15), ("Roar naked choke",10), ("1-2-kick combo",10)]
Saladin_Tuahihi =[
"Saladin", #firstname
"Tuahihi", #lastname
"The bun",#nickname
6,#boxing
4,#muay_thai
5,#wrestling
10,#bjj
10, #energy
Sk_create.map_to_objects(get_fightSkills(Saladin_Tuahihi_skills))
]
## TEST SK CREATION
#skill_obj_list = Sk_create.map_to_objects(Saladin_Tuahihi[8])
#for skill in skill_obj_list:
    #print(skill.name, skill.quantity)


test_skills = [("Jab", 10), ("Illegal move trap", 10), ("Powerjab", 5), ("Bearhug takedown", 10),\
                            ("Brute force sweep", 15), ("Roar naked choke",10), ("1-2-kick combo",10)]
Mr_test =[
"Mr Test", #firstname
"Tester", #lastname
"Mr Test",#nickname
6,#boxing
4,#muay_thai
5,#wrestling
10,#bjj
10, #energy
Sk_create.map_to_objects(get_fightSkills(test_skills))
]




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


