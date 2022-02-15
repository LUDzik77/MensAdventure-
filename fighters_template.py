from random import choices
import Skillcards_map_and_create as Sk_create
import Skillist_with_weights as Sk_list


def get_fightSkills(skillset_to_pick_from):
    string_list = choices([s[0] for s in skillset_to_pick_from], 
                          weights=[s[1] for s in skillset_to_pick_from], k=6)
    result =  list({i:string_list.count(i) for i in string_list}.items())
    return(result)


Saladin_Tuahihi =[
"Saladin", #firstname
"Tuahihi", #lastname
"The bun",#nickname
5,#boxing
5,#muay_thai
5,#wrestling
5,#bjj
8, #energy
Sk_create.map_to_objects(get_fightSkills(Sk_list.all_skills_equal_weights))
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
Sk_create.map_to_objects(get_fightSkills(Sk_list.wrestler_skills))
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


