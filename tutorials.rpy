python early:
    def tutorial_place(place):
        # to make it work update persistent.tutorial list in persistent_data with new tutorial_place's name
        if place not in persistent.tutorial:
            pass
        else:
            persistent.tutorial.remove(place)
            if place == "home": 
                renpy.say(K,"tutorial coming soon :) ")
            elif place == "gym": 
                renpy.say(K,"tutorial coming soon :) ")
            elif place == "out_of_city":
                renpy.say(K,"tutorial coming soon :) ")
            elif place == "disco_pub":
                renpy.say(K,"tutorial coming soon :) ")
            elif place == "university": 
                renpy.say(K,"tutorial coming soon :) ")
            elif place == "shop": 
                renpy.say(K,"tutorial coming soon :) ")
            elif place == "bed": 
                renpy.say(K,"tutorial coming soon :) ")
