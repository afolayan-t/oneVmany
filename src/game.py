import numpy as np
import random
import player_classes

class dbd:
    """Defines state of game"""
    num_games_run = 0
    def __init__(self, killer, survivors):
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
        print("Game Number: " + num_games_run)
        print("Survivors Alive: " + self.survivors_alive)
        print("Generators Fixed: " + self.gens_fixed)

    def hooked(players):

    def chase(players):

        probs = [[0.3,  0.4],
                 [0.05, 0.7],
                 [0.2,  0.3],
                 [0.7, 0.6],
                 [0.95,  0.3],
                 [0.8, 0.7]]

        num_chased = len(players) - 1
        playerChoice = players[0].


    def run_round(self):
        ''' Runs a single round of the game'''

        turns = random.shuffle(range(0, 5))
        for turn in turns:
            if turn == 4: 
                scenario = killer.nextMove()
            else: 
                scenario = survivors[turn].nextMove()

            if scenario[0] == "Chase":
                chase(scenario[1])
            if scenario[0] == "Hooked":
                hooked(scenario[1])
        return
            


    def play(self):
        ''' Runs rounds until game is over '''
        
        if survivors_alive == 0:
            return payoff([])


    def payoff(Outcome):
        ''' Takes list of survivors alive and rewards everyone accordingly '''
        

    def store_data():
        pass


    
    
