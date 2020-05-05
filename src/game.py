import numpy as np
import random
from player_classes.py import *

class dbd:
    """Defines state of game"""
    def __init__(self, killer, survivors):
        self.num_games_run = 0
        self.gen_set = list(np.zeros((7,3))) # 0 if not fixed, 1 if fixed, and player_object if being worked on
        self.door_set = list(np.zeros((2,1))) # doors that can be opened once 5 generators are fixed
        self.hook_set = list(np.zeros((4,2))) # 1 spot for hooked survivor, 1 spot for camping killer
        self.trap_door_open = False 


        self.num_rounds = 0
        self.free_survivors = survivors
        self.killer = killer

        self.survivors_alive = 4
        self.gens_fixed = 0


    
    def __repr__(self):
        print("Game Number: " + self.num_games_run)
        print("Survivors Alive: " + self.survivors_alive)
        print("Generators Fixed: " + self.gens_fixed)



    def fix_generator(self, choice):
        """accepts generator pick from survivor"""
        pass

    def open_door(self, choice):
        pass

    def hooked(self, players):
        pass


    def chase(self, players):

        chasedPlayer = players[0]

        if len(players) == 1:
            probs = {"Obstacle": 0.3, "Stun": 0.05, "Run": 0.2}
        else:
            probs = {"Obstacle": 0.4, "Stun": 0.7, "Run": 0.3}

        while(True):    
            
            playerStrat = chasedPlayer.strategicMove("Chase")
            chaseOutcome = np.random.binomial(1, probs[playerStrat])

            if chaseOutcome == 1: # Escaped
                chasedPlayer.score += 10
                return
            else:  # Hit by killer
                if not chasedPlayer.is_injured: # First hit -> continue chase
                    chasedPlayer.is_injured = True
                else: 
                    self.hook_set[random.randint(0,3)][0] = chasedPlayer
                    self.free_survivors.remove(chasedPlayer)
                    chasedPlayer.hooks += 1
                    camping = np.random.binomial(1, 0.5)
                    if camping: 
                        self.hook_set[random.randint(0,3)][1] = self.killer
                        self.killer.busy = True
                    return




    def run_round(self):
        ''' Runs a single round of the game'''

        # Killers and free survivors take turns to play in a random order
        for player in random.shuffle(self.free_survivors.append(self.killer)):
            scenario = player.nextMove()

            if scenario[0] == "Chase":
                self.chase(scenario[1])
            if scenario[0] == "Hooked":
                self.hooked(scenario[1])
            if scenario[0] == "Fix Gen":
                self.fix_generator(scenario[1])
            if scenario[0] == "Door":
                self.open_door(scenario[1])
        return
            


    def play(self):
        ''' Runs rounds until game is over '''
        
        if self.survivors_alive == 0:
            return payoff([])


    def payoff(self, Outcome):
        ''' Takes list of survivors alive and rewards everyone accordingly '''
        

    def store_data():
        pass


    
    
