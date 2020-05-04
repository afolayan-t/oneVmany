import numpy as np


class dbd:
    """Defines state of game"""

    def __init__(self, killer, surv_vect):
        self.gen_set = list(np.zeros((7,3))) # 0 if not fixed, 1 if fixed, and player_object if being worked on
        self.door_set = list(np.zeros((2,1))) # doors that can be opened once 5 generators are fixed
        self.trap_door_open = False 
        self.num_rounds = 0
        self.survivors = surv_vect
        self.killer = killer
    
    def __repr__(self):
        pass

    def run_round(self)
        #run generator picks
        #check how many generators are being worked on, and have been completed
        #check if chase has been entered this round
        #run skill checks
        

    def store_data():
        pass


    
    
