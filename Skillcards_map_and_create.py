#here we map skills from strings to objects

import Skillcards as Sk

def map_to_objects(list_of_objects_to_map):
    fighter_skillcards = []
    for to_map in list_of_objects_to_map:
        fighter_skillcards.append(get_1_Skillcard_object(to_map))
    return(fighter_skillcards)


def get_1_Skillcard_object(to_map):
    if to_map[0] == "Jab":
        new_object = Sk.Jab()
    elif to_map[0] == "Lowkick":
        new_object = Sk.Lowkick()
    elif to_map[0] == "Pull guard":
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
    elif to_map[0] == "Swing for the fences" :
        new_object = Sk.Swing_For_The_Fences()
    elif to_map[0] == "Slap":
        new_object = Sk.Slap()
    elif to_map[0] == "Highkick":
        new_object = Sk.Highkick()
    elif to_map[0] == "Flying knee":
        new_object = Sk.Flying_Knee()
    elif to_map[0] == "Armbar":
        new_object = Sk.Armbar()    
    elif to_map[0] == "Ground and pound":
        new_object = Sk.Ground_and_Pound()
    elif to_map[0] == "Dirty boxing":
        new_object = Sk.Dirty_Boxing()  
    elif to_map[0] == "Devastating overhand":
        new_object = Sk.Devastating_Overhand()
    elif to_map[0] == "Elbows":
        new_object = Sk.Elbows() 
    elif to_map[0] == "Windmill style":
        new_object = Sk.Windmill_Style()  
    elif to_map[0] == "Flying armbar":
        new_object = Sk.Flying_Armbar()
    elif to_map[0] == "Double leg":
        new_object = Sk.Double_Leg()
    elif to_map[0] == "Universal punch":
        new_object = Sk.Universal_Punch()
    elif to_map[0] == "Slam":
        new_object = Sk.Slam()   
    elif to_map[0] == "Single leg":
        new_object = Sk.Single_Leg()
    elif to_map[0] == "Trip kick":
        new_object = Sk.Trip_Kick()
    elif to_map[0] == "Technical stand up":
        new_object = Sk.Technical_Stand_Up()
    elif to_map[0] == "Front kick":
        new_object = Sk.Front_Kick()    
    elif to_map[0] == "Triangle choke":
        new_object = Sk.Triangle_Choke() 
    elif to_map[0] == "Leglock scramble":
        new_object = Sk.Leglock_Scramble()  
    elif to_map[0] == "Heel hook":
        new_object = Sk.Heel_Hook()
    elif to_map[0] == "Suplex":
        new_object = Sk.Suplex()      
    elif to_map[0] == "Knees in clinch":
        new_object = Sk.Knees_In_Clinch()          

        
        
    else: print(f"No skill <{to_map[0]}> to mappped by <get_Skillcard_object>")
    new_object.quantity = to_map[1]
    return(new_object)   


    