label shop:
scene bg shop
$ tutorial_place("shop")
menu:
    "Pewex 2.0":
        jump pewex
    "Lombard 'Sell your soul'":
        "we'll not buy your dirty pants dude, go elsewhere"
        jump shop
    "Lets visit a city":
        jump city

       
label pewex:
    menu:
        "object of desire":
            jump shop 
        "baseball set without a ball":
            jump shop