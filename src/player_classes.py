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
        self.player_strategy = player_strategy
        self.is_injured = False #defines if you hav been injured
        self.gens_completed = 0
        self.score = 0
        self.hooks = 0
        
        if player_strategy == "regular":
            self.help_p = .5 #probability to help
            self.soloist = True #defines whether agent prefers to be alone or not

        #num_survivors += 1
            

    def __repr__(self):
        print(player_name + " Strategy: " + self.player_strategy )
        print("Score: " + self.score)
        print(Score)
    
    def update_strategy(self, score, payoff):
        """Takes current game state and defines next rounds strategy based on this"""

        pass

    def strategicMove(self, situation):
        if situation == "Chased":
            return np.random.choice(["Run", "Obstacle", "Stun"],1, [1/3, 1/3, 1/3])[0]
        if situation == "Save":
            return np.random.choice(["Rescue", "Leave"],1, [1/2, 1/2])[0]



    def request_help(self):
        """requests help from a particular survivor"""
        
        pass

    def pick_gen(self, gen_set):
        num_avail_gens = len(gen_set)
        choice = random.int(0, num_avail_gens)
        return choice

    def help(self, survivor):
        """Helps survivor by unhooking or healing them"""

    def nextMove(self, game, gen_set, hook_set, door_set, is_chase = False, is_hooked = False):
        """Chooses whether to pick a generator to work on, or go and help a teammate"""
        help_p = self.help_p

        if self.is_injured == True:
            self.request_help()
            return
        if all(s==0 for s in hook_set) !=True: # not empty
            help_decision = np.random.binomial(1,help_p)
            if help_decision == 1: #agrees to help
                #pick survivor to help
                hooked_survivors = [survivor for survivor in hooks if survivor != 0]
                surv_choice = random.choice(hooked_survivors)
                self.help(surv_choice)
                return
        #pick generator
        if game.gens_fixed < 5
            available_gens = [gen for gen in gen_set if 0 in gen] # gives list of generators with available spot
            game.fix(self.pick_gen)
            return
        else:
            # open door
            if all(d==0 for d in door_set):
                door_choice = random.choice(door_set)
                game.open_door(door_choice)
            else:# door is already being opened, nothing else to do
                return
            


class killer:

    def __init__(killer_strategy):
        """Defines Killer"""
        self.busy = False

    def check_gen(self, gen_set):
        """"""

    def pick_survivor(self, survivors_discovered):
        """once a set of survivors have been discovered, picks a survivor to chase from set"""

    def nextMove(self, gen_set, hook_set, survivors, is_chase = False):
