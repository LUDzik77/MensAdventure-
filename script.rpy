
####check:
#define config.menu_include_disabled = False

$_rollback = False  #it should disable rollback but it isn't working


define K = Character("Kamilion", color="#E03B8B")
define _K = Character("Kamilion", kind=nvl, color="#E03B8B")
define L = Character("Leo", color="#E03B8B")
define O = Character("Orszula", color="#E03B8B")
define n = Character(what_italic=True)
define _nvl = Character('', kind=nvl, color="#c8ffc8")
define _v = Character('The voice', kind=nvl, color="#c8ffc8")
image Kamilion = im.Scale("images/characters/Kamilion1.jpg", 600, 800)


label start:
    call variables_start
    show Kamilion
    #### python:
        #### import fightgame
        ###renpy.say("", fightgame.result_)


    K "current version: [config.version]"
    jump city
     

label city:
    scene bg_krakow
    show screen city_navigationUI
    pause
    jump city

