import numpy as np

"""class player:
    def __init__():"""
#adding items medkit(1-self heal), toolbox, 
class survivor:
    
    def __init__(player_strategy):
        """Defines Survivor strategy; selfless, selfish, trust, random, & adaptive*"""
        self.help_p = .5 #probability to help
        self.betray_p = .5 #probability to betray
        self.soloist = True #defines whether agent prefers to be alone or not
        self.is_injured = False #defines if you hav been injured
        self.score = 0

    def __repr__(self):
        pass 
    
    def update_strategy(self, score, payoff):
        """Takes current game state and defines next rounds strategy based on this"""
        pass

    def request_help(self):
        pass

    def pick_gen(self, gen_set):
            
        pass

    def work_on_gen(self)


    def take_action(self, gen_set):

class killer:

    def __init__(killer_strategy):
        """Defines Killer"""

    def check_gen(self, gen_set):
        """"""

    def pick_survivor(self, survivors_discovered):
        """once a set of survivors have been discovered, picks a survivor to chase from set"""