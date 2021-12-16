#here we map skills from strings to objects

import Skillcards as Sk

def map_to_objects(list_of_objects_to_map):
    fighter_skillcards = []
    for to_map in list_of_objects_to_map:
        fighter_skillcard.append(get_Skillcard_object(to_map))
    return(fighter_skillcards)


def get_Skillcard_object(to_map):
    if to_map[0] == "Jab":
        new_object = Sk.Jab()
    elif to_map[0] == "Lowkick":
        new_object = Sk.Lowkick()
    elif to_map[0] == "Pullguard":
        new_object = Sk.Pullguard()    
    elif to_map[0] == "Bearhug takedown":
        new_object = Sk.Bearhug_Takedown()        
    elif to_map[0] == "1-2-kick combo":
        new_object = Sk.One_Two_Kick_Combo()       
    elif to_map[0] == "Powerjab":
        new_object = Sk.Powerjab()      
    elif to_map[0] == "Lay and pray":
        new_object = Sk.Lay_And_Pray()  
    elif to_map[0] == "Brute force sweep":
        new_object = Sk.Brute_Force_Sweep()  
    elif to_map[0] == "Illegal move trap":
        new_object = Sk.Illegal_Move_Trap()
    elif to_map[0] == "Roar naked choke":
        new_object = Sk.Roar_Naked_Choke()
    elif to_map[0] == "Lucky punch":
        new_object = Sk.Lucky_Punch()
    elif to_map[0] == "Granite chin":
        new_object = Sk.Granite_Chin()
    elif to_map[0] == "Cardio king":
        new_object = Sk.Cardio_King()
    new_object.quantity = to_map[1]
    return(new_object)
        


    