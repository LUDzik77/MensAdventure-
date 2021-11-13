label home:
scene bg home
$ tutorial_place("home")
menu:
    "your PC":
        jump computer
    "your ideas":
        jump ideas
    "parents":
        jump parents
    "Jump to the bed":
        jump bed
    "Lets visit a city":
        jump city


label computer:
    $ renpy.notify("you turned your pc on")
    menu:
        "turn off pc":
            $ renpy.notify("you turned your pc off")
            jump home
        "play a game":
            jump pc_game

label pc_game:
    "click click click... you won"
    jump home

label parents:
    "mum, dad... cya"
    jump home

label ideas:
    menu:
        "thought cabinet":
            jump thought_cabinet
        "let me think about...":
            jump meditate
        "end the meditation":
            jump home

label thought_cabinet:
    show Kamilion
    python:
        x="{b}\nYOUR THOUGHT CABINET:\n\n\n{/b}"
        y="\n".join(persistent.thought_cabinet)
        renpy.say(_nvl,"[x]")
        renpy.say(_nvl,"[y]")
        
    nvl clear
    jump home

label meditate:
    "Here you can shape yourself..."
    jump home

label bed:
    $ tutorial_place("bed")
    $ quote= show_slow(bedroom_quotation)()
    "[quote]"
    $ add_time(2)
    $ change_health(2)
    $ persistent.delays = []
    jump home