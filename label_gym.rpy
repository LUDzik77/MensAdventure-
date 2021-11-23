label gym:
scene bg gym
$ tutorial_place("gym")
        
## https://www.renpy.org/doc/html/screen_special.html#choice-screen  ### <------------------check it out, solution!
## https://www.renpy.org/doc/html/menus.html <-- and the base thing
## https://www.renpy.org/doc/html/screen_special.html#choice-screen #later on
#example: how to make choice and saved  it in the variable
###$result = renpy.display_menu([ ("East", "-east"), ("West", "-west") ])
$ not_delayed = True if "training" not in persistent.delays else False
menu:
    "look around":
    #this one will be more advanced
        "sweet sweat cave babe... you see Leo and "
        $persistent.leo = True
        jump gym
    "Talk with Leo" if persistent.leo:
        "Hi am Leo"
        jump gym
    "Lets visit a city":
        jump city
    "train --> gym" if not_delayed:
        $ train_gym(1)
        jump training
    "train --> boxing" if not_delayed:
        $ train_boxing(1)
        jump training
    "train --> muay thai" if not_delayed:
        $ train_muay_thai(1)
        jump training 
    "train --> wrestling" if not_delayed:
        $ train_wrestling(1)
        jump training
    "train --> bjj" if not_delayed:
        $ train_bjj(1)
        jump training


label training: 
    $ renpy.notify("You are tired as hell")
    "You've participate in the training session. \nNow you are covered in sweat. \nOh gosh it was worth it!"
    $ persistent.delays.append("training") 
    jump gym
    
# Mr.Hoopoe
# Animax & Animin /Animal
# 
