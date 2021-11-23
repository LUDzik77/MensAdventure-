label variables_start:

# REMOVE the line below on production (or if you need to test)
    $ persistent._clear(progress=False)

    $ if persistent.tutorial is None: persistent.tutorial = ["home", "gym", "disco_pub", "shop", "out_of_city", "university", "bed"]

 
# thought_cabinet is visible 4 player in home/thought_cabinet
# and represents ideas adopted by our hero, which can trigger events/dialog options etc
    $ if persistent.thought_cabinet is None: persistent.thought_cabinet = []
    #["video gamer", "pleasure seeker", "well educated", "catholic zelot"]
# "Conspiracy theorist" 
# "Religious zealot" (political stance)


# teasers are ideas of our hero, which can became part of his psycho (part of cabinet_of_thoughts) or trigger quests etc.
# persistent.teasers_fullfilled store all the teasers that shold not be activated  anymore
    $ if persistent.teasers is None: persistent.teasers = ["My goals"]
    $ if persistent.teasers_fullfilled is None: persistent.teasers_fullfilled = []
# here is the list of teasers with a  notification if they are fully implemented:
# "My goals"            90%
# "StarCraft"           ---> ongoing work
# "King of Dragon Pass" ---> ongoing work
# "Life is a simulation"80%
# "Secret lover"        80%
# "That damn voice"     ---> not implemented
# "Realist"             ---> not implemented
# "Pesimist"            ---> not implemented
# "Optimist"            ---> not even added
# "What was that!"      90%

# knowledgebase saves finished courses from university, and few other skills
# we can get a perks "somehow educated", "well educated", "egghead" thanks to education in cabinet_of_thoughts
    $ if persistent.knowledgebase is None: persistent.knowledgebase = []
# the class you are signed up at the moment /options are:/to be done/
    # $ if persistent.signedclass is 

# for now TIME is just a growing number, when we reach 1000 it is game over.
    $ if persistent.time is None: persistent.time = 0
# delays are added for activities to avoid click-spam. Delays are removed after sleeping <bed>
# one instance of delay for activity.
    $ if persistent.delays is None: persistent.delays = []
    
    $ if persistent.money is None: persistent.money = 10
# List of property is list of all your objects (food as well as real estate) 
# it is in form of  list of 2 element lists (object name + quantity)
    $ if persistent.property is None: persistent.property = [["leather jacket", 1]]
    
# for now health is both mental and physical; ideais to have test K100, so it is like percentage
    $ if persistent.health is None: persistent.health = 95
    
# flags that unlocks content or progress
# we can turn them here for test
    # $ persistent.leo is True
    # $ persistent.orszula is True
    # $ persistent.fight is True
    # $ persistent.zoya is True
    
    
    
    $ if persistent.boxing is None: persistent.boxing = 1
    $ if persistent.muay_thai is None: persistent.muay_thai = 1
    $ if persistent.wrestling is None: persistent.wrestling = 1
    $ if persistent.bjj is None: persistent.bjj = 1
    
    
    
    
    