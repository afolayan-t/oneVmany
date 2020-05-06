import numpy as np
import random


"""class player:
    def __init__():"""
#adding items medkit(1-self heal), toolbox, 
class survivor:
    num_survivors = 0
    def __init__(self, player_name, player_strategy):
        """Defines Survivor strategy; selfless, selfish, trust, random, & adaptive*"""
        #self.survivor_num = num_survivors + 1
        self.player_name = player_name
        self.player_strategy = player_strategy

        self.is_injured = False #defines if you hav been injured
        self.gens_completed = 0
        self.score = 0
        self.hooks = 0
        
        if player_strategy == "regular":
            self.help_p = .5 #probability to help
            self.r =.1
            self.soloist = True #defines whether agent prefers to be alone or not

        #num_survivors += 1
            

    def __repr__(self):
        print(self.player_name + " Strategy: " + self.player_strategy )
        print("Score: " + self.score)
        print(self.score)
    
    #def update_strategy(self, score, payoff):
    #    """Takes current game state and defines next rounds strategy based on this"""
    #    pass

    def strategicMove(self, situation):
        if situation == "Chased":
            return np.random.choice(["Run", "Obstacle", "Stun"],1, [1/3, 1/3, 1/3])[0]
        if situation == "Save":
            return np.random.choice(["Rescue", "Leave"],1, [1/2, 1/2])[0]
        if situation == "Pop":
            return np.random.choice(["Continue", "Leave"],1, [1/2, 1/2])[0]
        if situation == "Help":
            return np.random.choice(["Heal", "Ignore"],1, [1/2, 1/2])[0]
        



    def request_help(self, game):
        """requests help from a particular survivor"""

        for survivor in random.shuffle(game.free_survivors):
            x = survivor.strategicMove("Help")
            if x == "Heal":
                self.is_injured == False
                return
            else:
                return



    def pick_gen(self, gen_set):
        num_avail_gens = len(gen_set)
        choice = random.randint(0, num_avail_gens)
        return choice


    def nextMove(self, game):
        """Chooses whether to pick a generator to work on, or go and help a teammate"""

        if self.is_injured == True:
            self.request_help(game)
            if self.is_injured == False:
                return ("Hide", self)
        if all(s==0 for s in game.hook_set) !=True: # not empty
            help_decision = np.random.binomial(1,self.help_p)
            if help_decision == 1: #agrees to help
                #pick survivor to help
                hooked_survivors = [survivor for survivor in game.hook_set[:,0] if survivor != 0]
                surv_choice = random.choice(hooked_survivors)
                return ("Hooked", [self, surv_choice[0]])
        #pick generator
        if game.gens_fixed < 5:
            available_gens = [gen for gen in game.gen_set if 0 in gen] # gives list of generators with available spot
            return ("Fix Gen", self, self.pick_gen(available_gens))
        else:# nothing left to do
            if game.gens_fixed < 5 & game.survivors_alive == 1:
                return("Trapdoor", self) #search for Trapdoor
            else:
                return ("Hide", self)
            


class killer:

    def __init__(self):
        """Defines Killer"""
        self.busy = False
        self.camp_p = .5

    def check_gen(self, gen_set):
        """"""
        choice = np.random.choice(range(len(gen_set)))
        return choice


    def nextMove(self, game):
        """takes in game opject"""
        gen_set = game.gen_set
        if self.busy == True:
            return ("Nothing", None)
        else:
            #check generator
            choice = self.check_gen(gen_set)
            picked_gen = gen_set[choice,:]
            found_survivors = [surv for surv in picked_gen if surv != 0]
            if len(found_survivors) != 0:
                if len(found_survivors) == 1:
                    return ("Chase", found_survivors)
                else:
                    return ("Chase", found_survivors[:2])

        for survivor in random.shuffle(game.free_survivor):
            search = np.random.binomial(1,survivor.r)
            if search == 1:
                return ("Chase", survivor)
        return ("Nothing", None)
