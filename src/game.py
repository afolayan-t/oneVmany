import numpy as np
import * from player_classes

class dbd:
    """Defines state of game"""
    num_games_run = 0
    def __init__(self, killer, surv_vect):
        self.gen_set = list(np.zeros((7,3))) # 0 if not fixed, 1 if fixed, and player_object if being worked on
        self.door_set = list(np.zeros((2,1))) # doors that can be opened once 5 generators are fixed
        self.hook_set = list(np.zeros((4,2))) # 1 spot for hooked survivor, 1 spot for camping killer
        self.trap_door_open = False 


        self.num_rounds = 0
        self.free_survivors = surv_vect
        self.killer = killer

        self.survivors_alive = 4
        self.gens_fixed = 0


    
    def __repr__(self):
        print("Game Number: " + num_games_run)
        print("Survivors Alive: " + self.survivors_alive)
        print("Generators Fixed: " + self.gens_fixed)

    def fix_generator(choice):
        """accepts generator pick from survivor"""

    def open_door(choice):

    def run_round(self):
        #define gen pick order
        #run generator picks
        #check how many generators are being worked on, and have been completed
        #check if chase has been entered this round
        #run skill checks
        

    def store_data():
        pass


    
    
