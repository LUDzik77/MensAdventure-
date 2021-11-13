label gym:
scene bg gym
$ tutorial_place("gym")
        
## https://www.renpy.org/doc/html/screen_special.html#choice-screen  ### <------------------check it out, solution!
## https://www.renpy.org/doc/html/menus.html <-- and the base thing
## https://www.renpy.org/doc/html/screen_special.html#choice-screen #later on
#example: how to make choice and saved  it in the variable
###$result = renpy.display_menu([ ("East", "-east"), ("West", "-west") ])

menu:
    "pump your muscles":
        "sweet sweat cave babe... you see Leo"
        $persistent.leo = True
        jump gym
    "Talk with Leo" if persistent.leo:
        "Hi am Leo"
        jump gym
    "Lets visit a city":
        jump city
        

        
# Mr.Hoopoe
# Animax & Animin /Animal
# 
