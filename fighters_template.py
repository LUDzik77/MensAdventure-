from random import choices
import Skillcards_map_and_create as map_

#we need a mechanism to generate Skillcards and set quantity FROM the  list below 
#this list should have the same format as player skilllist in the main game.... but we need to apply weights   # NEED MORE WORK
#Saladin_Tuahihi_skills = # with weights
Saladin_Tuahihi_skills_temp = map_.map_to_objects([("Jab",1), ("Illegal move trap",1)], ("Jab",1))

Saladin_Tuahihi_s_weights = [10,10,10]
Saladin_Tuahihi =[
"Saladin", #firstname
"Tuahihi", #lastname
"The bun",#nickname
6,#boxing
4,#muay_thai
5,#wrestling
10,#bjj
10, #energy
choices(Saladin_Tuahihi_skills, weights=Saladin_Tuahihi_s_weights, k=5)
]


#import inspect
#import Skillcards
#[m[0] for m in inspect.getmembers(Skillcards, inspect.isclass) if m[1].__module__ == 'Skillcards.py']

