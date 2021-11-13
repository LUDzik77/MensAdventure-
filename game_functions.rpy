
python early:
    import random
# TIME
    def add_time(time):
        persistent.time += time
    
    def time_elapsed():
        result = float(persistent.time)/10
        if result<0: return(0)
        else: return(result)
        
        
# HEALTH
    def change_health(number):
        persistent.health += number
        
    def describe_health():
        if persistent.health>99: return('unbreakable')
        elif persistent.health>83:return('solid')
        elif persistent.health>70: return('so so')
        elif persistent.health>55: return('terrible')
        else: return('barely alive')
    
        
# MARTIAL ARTS   
    def train_boxing(skill):
        persistent.boxing += skill
        add_time(1)
        persistent.health -= skill
    
    def train_muay_thai(skill):
        persistent.muay_thai += skill
        add_time(1)
        persistent.health -= skill
        
    def train_wrestling(skill):
        persistent.wrestling += skill
        add_time(1)
        persistent.health -= skill
    
    def train_bjj(skill):
        persistent.bjj += skill
        add_time(1)
        persistent.health -= skill



    def show_slow(func):
        def inside():
            q = func()
            return("{cps=25}" + q + "{/cps}")
        return(inside)


# SLEEPING
    @show_slow
    def bedroom_quotation():
        quotes = ["Sweet dream are made of this", "Exit light enter night",
                  "Wake the fuck up samurai. We have a city to burn!",
                  "And I know that in the morning I will wake up in the shivering cold",
                  "So wake me up when it's all over ", "Wake me up before you go-go",
                  "Day after day your home life's a wreck...", 
                  "My spirit's sleeping somewhere cold until you find it there and lead it back home",
                  "It's now or never, I ain't gonna live forever"
                  ]
        
        edited_quote = random.choice(quotes)
        return(edited_quote)

        



