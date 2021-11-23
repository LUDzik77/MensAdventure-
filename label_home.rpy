label home:
scene bg home
$ tutorial_place("home")
menu:
    "your PC":
        jump computer
    "your ideas":
        jump ideas
    "your property":
        jump property
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
    menu:
        "StarCraft":
            "Terran marines still imba!"
            $ add_teaser("StarCraft")
        "King of The Dragon Pass":
            "omg, thats the best game I've ever played"
            $ add_teaser("King of Dragon Pass")
    #"[persistent.teasers]"
    jump home

label parents:
    "mum, dad... cya"
    jump home

label ideas:
    menu:
        "thought cabinet":
            jump thought_cabinet
        "let me think about..." if len(persistent.teasers)!=0:
            jump meditate
        "end the meditation":
            jump home

label thought_cabinet:
    show Kamilion
    nvl clear
    python:
        x="{b}\nYOUR THOUGHT CABINET:\n\n\n{/b}"
        y="\n".join(persistent.thought_cabinet)
        renpy.say(_nvl,"[x]")
        renpy.say(_nvl,"[y]")
    nvl clear
    #"[persistent.thought_cabinet]"
    jump home


label property:
    " here will be your inventory :) "
    jump home

label bed:
    $ tutorial_place("bed")
    $ quote= show_slow(bedroom_quotation)()
    "[quote]"
    $ add_time(2)
    $ change_health(2)
    $ persistent.delays = []
    jump home
    
    
label meditate:
    nvl clear
    menu(nvl=True):
        _nvl "Here you can shape yourself"
        #nvl hide dissolve
        #nvl show dissolve
        #"[persistent.teasers]"
        #nvl clear
        "My goals" if check_teaser("My goals"):
            jump My_goals
        "Life is a simulation" if check_teaser("Life is a simulation"):
            jump Life_is_a_simulation
        "There are secrets everywhere!"  if check_teaser("Secret lover"):
            jump There_are_secrets_everywhere
        "Old good games" if check_teaser("King of Dragon Pass"):
            jump Old_good_games
        "Modern shitty games" if check_teaser("StarCraft"):
            jump Modern_shitty_games
        "What was that!" if check_teaser("What was that!"):
            jump What_was_that
    jump home
    
    
label My_goals:   
    nvl clear
    _K "What am I doing here?"
    _v "I feel it's like a game..."
    _nvl"What is even the purpose for being here?"
    _K "What I have to do?"
    _nvl "University? Shopping? Gym? Or I'll get out of city?"
    _v "I have to figure it out..."
    nvl clear
    menu(nvl=True):
        _K "I really wanna know what to do!"
        "Sure i do! Gimme the solution right now":
            _v "This game has no single goal. It is the sudo life simulation."
            $ add_teaser("Life is a simulation")
        "I love secrets, let me discover the world":
            $ add_teaser("Secret lover")
            pass
    _v "Walk around and feel the magic"
    _nvl "Try to enter same places more than once. You might unlock new options or trigger an event."
    _nvl "Sometimes your personality (-->thought_cabinet) can make a difference"
    _nvl "If all hopes are gone... just take rest (--> go to bed) and look what will happen"
    _v "See you soon :)"
    $ use_teaser("My goals")
    jump home

label Life_is_a_simulation:    
    _v "Hello again"
    $ use_teaser("Life is a simulation")
    menu(nvl=True):
        "Hello":
            _K "Hello"
            jump conspiration_life_simulation
        "Who are you?":
            _K "Who are you?"
            _v "Good question: Who are you?"
            menu(nvl=True):
                "Ok, forget it":
                    _K "Ok, forget it"
                    jump conspiration_life_simulation
                "I asked you something":
                    _K "I asked you something"
                    _v "I am the Voice. It have to be enough for now."
                    $ add_teaser("That damn voice")
                    "Do you want to talk about secrets or not?"
                    menu(nvl=True):
                        "I will discover them on my own":
                            jump home
                        "go on...":
                            _K "go on..."
                            jump conspiration_life_simulation
        "Go away":
            jump home
    
label There_are_secrets_everywhere:  
    _v "Hello again"
    $ use_teaser("Secret lover")
    menu(nvl=True):
        "Hello":
            _K "Hello"
            jump conspiration_secrets_everywhere
        "Who are you?":
            _K "Who are you?"
            _v "Good question: Who are you?"
            menu(nvl=True):
                "Ok, forget it":
                    _K "Ok, forget it"
                    jump conspiration_secrets_everywhere
                "I asked you something":
                    _K "I asked you something"
                    _v "I am the Voice. It have to be enough for now."
                    $ add_teaser("That damn voice")
                    _nvl "Do you want to talk about secrets or not?"
                    menu(nvl=True):
                        "I will discover them on my own":
                            jump home
                        "go on...":
                            _K "go on..."
                            jump conspiration_secrets_everywhere
        "Go away":
            jump home 
    
label conspiration_secrets_everywhere:
    _v "There are secrets hidden here and there"
    menu(nvl=True):
        "I realize it. Bye":
            _K "I love it. Thx for that information"
            $ add_teaser("Realist")
            jump home
        "Is someone controlling our lives?": 
            _K "Is someone controlling our lives?"
            menu(nvl=True):
                "No one specific":
                    _v "No one specific"
                    _K "Oh that's good news..."
                    jump conspiration_life_simulation
                "Aliens of course":
                    _v "Aliens of course"
                    _K "You're jokin..."
                    menu(nvl=True):
                        "Sure":
                            _v "Sure"
                            _K "So stop bothering me!"
                            $ add_teaser("That damn voice")
                            jump home
                        "now you know":
                            _v "now you know"
                            $ extend_personality("Conspiracy theorist")
                            "Sudden shivers leave you speechless"
                            jump home
                "Postmodern marxists for sure":
                    _v "Postmodern marxists for sure"
                    _K "It sounds a bit silly..."
                    _v "Though you do believe such a nonsense?"
                    menu(nvl=True):
                        "I'm serious!":
                            _K "I'm serious!"
                            $ extend_personality("Conspiracy theorist")
                            "Sudden shivers leave you speechless"
                            jump home
                        "I'm fooled by media":
                            _K "I'm fooled by media"
                            $ add_teaser("Realist")
                            jump home
                        "Whatever... marxists can be cool":
                            _K "Whatever... marxists can be cool"
                            $ add_teaser("Optimist")
                            jump home
        "That is amazing! It'll be hell a lot of fun finding all that lil' treasures!":
            _v "Your wellcome"
            _K "Excuse me, world is waiting!"
            $ add_teaser("Optimist")
            jump home
        "What kind of secrets?":
            _K "What kind of secrets?"
            menu(nvl=True):
                "That life is just a simulation": 
                    _v "That life is just a simulation"
                    _K "No it isn't!"
                    jump conspiration_life_simulation
                "That New World Order is coming":
                    _v "That New World Order is coming"
                    menu(nvl=True):
                        "That is the dumbest idea i've heard in that decade":
                            _K "That is the dumbest idea i've heard in that decade"
                            _v "You are the dumbest man..."
                            _K "Can you stop it?"
                            _v "Exactly"
                            $ add_teaser("That damn voice")
                            jump home
                        "You loudly swallow your saliva...": 
                           "You loudly swallow your saliva..."
                           $ extend_personality("Conspiracy theorist")
                           "Sudden shivers leave you speechless"
                           jump home
                "That it is all about you":
                    jump conspiration_life_simulation
                "I was joking. There are no secrets man. Life is long, rough and often miserable":    
                    _v "I was joking. There are no secrets man. Life is long, rough and often miserable"
                    _K "Kind of true, I cannot deny it..."                   
                    $ add_teaser("Realist")
                    $ add_teaser("Pesimist")
                    jump home
    jump home
    
label conspiration_life_simulation:
    _v "How to say it..."
    _nvl "It's all about you"
    _K "What do you mean by 'all'?"
    _v "All around you"
    _nvl "You're feeling a bit like Alice, tumbling down the rabbit hole?"
    _nvl "You have that feeling that your experience is not authentic..."
    menu(nvl=True):
        "what the hell you're talking about!":
            _K "what the hell you're talking about!"
            _v "..."
            $ add_teaser("What was that!")
            jump home
        #"I am miserable piece of shit":
        "kind of...":
            _K "kind of..."
            pass
    _V "You're here because you know something. What you know you can't explain."
    _nvl "But you feel it..."
    _nvl "That home is not your home. That gym does not exist and shop sells some crazy quirks."
    _nvl "You are not the true master of your life"
    _nvl "Now you can express it freely."
    _nvl "It's on the tip of your tongue."
    menu(nvl=True):
        "I am in the game":
            $ extend_personality("Conspiracy theorist")
            _K "I am in the game" 
            $ choice = renpy.display_menu(enterescapequit)
            jump home
        "There is a lord in heaven.":
            $ extend_personality("Religious zealot")
            _K "There is a lord in heaven."
            jump home
        "I don't like the idea that I'm not in control of my life":
            _K "I don't like the idea that I'm not in control of my life"
            jump home
    jump home

label What_was_that:
    $ use_teaser("What was that!")
    _K "What i have just experienced?"
    _nvl "No idea"
    $ renpy.notify("it was a joke or what?")
    jump home

label Old_good_games: 
    nvl clear
    _nvl "King of Dragon Pass"

label Modern_shitty_games:
    nvl clear
    _nvl "sc2" 