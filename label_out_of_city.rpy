label out_of_city:
scene bg out_of_city
$ tutorial_place("out_of_city")
menu:
    "Lets go out of da city":
        "countryside. Pigs and mud."
        jump out_of_city
    "Lets visit a city":
        jump city