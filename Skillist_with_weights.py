#ABOUT THOSE LISTS:
# list of skill with weights from which we random pick skillset (6) to fight
# TODO: a lot of lists to organise prepare the skillcards for type of fighters: drunken, wrestler, un-orthodox, grappler etc
all_skills_equal_weights = [
    ("Jab",4),
    ("Lowkick",4),
    ("Pull guard",4),           
    ("Bearhug takedown",4),
    ("1-2-kick combo",4),
    ("Powerjab",4),           
    ("Lay and pray",4),
    ("Brute force sweep",4),
    ("Lucky punch",4),         
    ("Granite chin",4),        
    ("Cardio king",4),
    ("Swing for the fences",4),
    ("Windmill style",4),
    ("Slap",4),
    ("Highkick",4),            
    ("Flying knee",4),          
    ("Roar naked choke",4),
    ("Armbar",4),
    ("Ground and pound",4),
    ("Dirty boxing",4),        
    ("Devastating overhand",4), 
    ("Elbows",4),               
    ("Flying armbar",4),        
    ("Double leg",4),
    ("Universal punch",4),      
    ("Slam",4),                 
    ("Single leg",4),           
    ("Trip kick",4),            
    ("Technical stand up",4),
    ("Front kick",4),           
    ("Triangle choke",4),       
    ("Leglock scramble",4),     
    ("Heel hook",4),           
    ("Suplex",4),               
    ("Knees in clinch",4),
    ("Sit out spin",4),        
    ("Guillotine",4),
    ("Bjj shrimp",4),          
    ("Crucifix",4),             
    ("Hammerfists",4),          
    ("GnP elbows",4),           
    ("Uppercut",4),             
    ("Drunkenjitsu",4),        
    ("Superman punch",4),       
    ("Footwork",4),             
    ("Grappling tricks",4),     
    ("Kata guruma",4) ,         
    ("Lure brawler",4),         
    ("Girly blows",4),
    ("Killer instinct",4),       
    ("Jab jab cross",4),
    ("Mount position", 4),
    ("Sprawl",4)
]


all_common_skills = [
    ("Jab",4),
    ("Lowkick",4),
    ("Bearhug takedown",4),
    ("1-2-kick combo",4),
    ("Lay and pray",4),
    ("Brute force sweep",4),
    ("Cardio king",4),
    ("Swing for the fences",4),
    ("Windmill style",4),
    ("Slap",4),
    ("Roar naked choke",4),
    ("Armbar",4),
    ("Ground and pound",4),
    ("Double leg",4),
    ("Technical stand up",4),
    ("Knees in clinch",4),
    ("Guillotine",4),
    ("Girly blows",4),
    ("Jab jab cross",4),
    ("Sprawl",4)
]

all_uncommon_skills = [
    ("Pull guard",4),           
    ("Powerjab",4),             
    ("Granite chin",4),         
    ("Highkick",4),             
    ("Dirty boxing",4),         
    ("Devastating overhand",4), 
    ("Single leg",4),           
    ("Trip kick",4),            
    ("Front kick",4),           
    ("Triangle choke",4),       
    ("Leglock scramble",4),     
    ("Heel hook",4),            
    ("Sit out spin",4),         
    ("Bjj shrimp",4),           
    ("GnP elbows",4),           
    ("Uppercut",4),             
    ("Footwork",4),             
    ("Grappling tricks",4),     
    ("Killer instinct",4),      
]


all_rare_skills = [
    ("Lucky punch",4),          
    ("Flying knee",4),          
    ("Elbows",4),               
    ("Flying armbar",4),        
    ("Universal punch",4),      
    ("Slam",4),                 
    ("Suplex",4),               
    ("Crucifix",4),             
    ("Hammerfists",4),          
    ("Drunkenjitsu",4),         
    ("Superman punch",4),       
    ("Kata guruma",4) ,         
    ("Lure brawler",4),
    ("Mount position", 4)
]




wrestling_skills = [
    ("Jab",2),      
    ("Bearhug takedown",6),
    ("1-2-kick combo",1),       
    ("Lay and pray",3),
    ("Brute force sweep",3),  
    ("Granite chin",2),        
    ("Swing for the fences",2),
    ("Roar naked choke",1),
    ("Armbar",1),
    ("Universal punch",2),   
    ("Ground and pound",5),
    ("Dirty boxing",10),        
    ("Devastating overhand",2),                  
    ("Double leg",4),
    ("Slam",3),                 
    ("Single leg",7),                  
    ("Technical stand up",1),             
    ("Suplex",4),               
    ("Knees in clinch",1),
    ("Sit out spin",3),        
    ("Guillotine",4),                 
    ("Hammerfists",1),          
    ("GnP elbows",1),                        
    ("Grappling tricks",1),     
    ("Kata guruma",1) ,              
    ("Girly blows",1),
    ("Killer instinct",2),       
    ("Jab jab cross",2),
    ("Mount position", 6),
    ("Sprawl",3)
]

bjj_skills = [
        ("Lowkick",1),
        ("Pull guard",4),           
        ("1-2-kick combo",1),       
        ("Lay and pray",1),
        ("Brute force sweep",2),
        ("Lucky punch",1),            
        ("Cardio king",1),
        ("Windmill style",1),
        ("Highkick",1),                 
        ("Roar naked choke",4),
        ("Armbar",4),
        ("Ground and pound",2),   
        ("Elbows",1),               
        ("Flying armbar",3),        
        ("Double leg",3),
        ("Universal punch",1),                   
        ("Single leg",1),           
        ("Trip kick",1),            
        ("Technical stand up",1),
        ("Front kick",2),           
        ("Triangle choke",4),       
        ("Leglock scramble",4),     
        ("Heel hook",4),           
        ("Suplex",1),               
        ("Knees in clinch",1),
        ("Sit out spin",1),        
        ("Guillotine",4),
        ("Bjj shrimp",4),          
        ("Crucifix",3),             
        ("Hammerfists",1),          
        ("GnP elbows",1),                     
        ("Drunkenjitsu",1),        
        ("Grappling tricks",4),     
        ("Kata guruma",2) ,         
        ("Lure brawler",2),         
        ("Girly blows",1),      
        ("Jab jab cross",4),
        ("Mount position", 1)
    ]


basic_wrestler = [
4,#boxing
3,#muay_thai
7,#wrestling
4,#bjj
6, #energy
]

basic_bjj= [
2,#boxing
4,#muay_thai
4,#wrestling
7,#bjj
7, #energy
]

basic_boxer = [
7,#boxing
3,#muay_thai
4,#wrestling
3,#bjj
7, #energy
]

basic_muay_thai = [
4,#boxing
7,#muay_thai
3,#wrestling
4,#bjj
6, #energy
]