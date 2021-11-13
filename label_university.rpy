label university:
scene bg university
$ tutorial_place("university")
menu:
    "sign up for a class" if not persistent.signedclass:
        jump chooseclass
    "participate in a [persistent.signedclass] class" if persistent.signedclass:
        "you listen what prof wants to say"
        $ persistent.delays.append(persistent.signedclass)
        jump university
    "take a walk around":
        "what the incredible university!"
        jump university
    "Lets visit a city":
        jump city
        
        
        
label chooseclass:
    
    menu:
        "Choose what do you want to study?"
        "English philology":
            "You pay proper amount of quids to sign up documents and take a sip of a tea... Oh mate, choosing any other faculty would be dodgy, wouldn't it?"
            $ persistent.signedclass =  "English philology"
            jump university
        "Sociology":
            K "By the power of Durkheim, Weber & Comte. I have the power!"  
            $ persistent.signedclass =  "Sociology"
            jump university