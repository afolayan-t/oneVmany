import numpy as np
import random
<<<<<<< HEAD
import * from player_classes.py
=======
from player_classes import *
>>>>>>> 2efed448e4a482850dc1d54adfb3355aeb8cd027

class dbd:
    """Defines state of game"""
   
    def __init__(self, killer, survivors):
        self.gen_set = list(np.zeros((7,3))) # 0 if not in use, 1 if fixed, player_object if being worked on
        self.gen_vals = list(np.zeros((7))) # 0 if not fixed, 3 if fixed
        self.hook_set = list(np.zeros((4,2))) # 0 if not in use, 1 if used, player_object if hooked
        self.trap_door_open = False 

        self.num_rounds = 0
        self.free_survivors = survivors
        self.dead_survivors = []
        self.killer = killer

        self.survivors_alive = 4
        self.gens_fixed = 0
        self.canEscape = 2 # After all generators fixed, players must wait 2 rounds before being able to escape

#------------------------------------------------------------

    
    def __repr__(self):
        print("Game Number: " + self.num_games_run)
        print("Survivors Alive: " + self.survivors_alive)
        print("Generators Fixed: " + self.gens_fixed)

#------------------------------------------------------------

    def lookForTrapDoor(self, player):
        Found = np.random.binomial(1, 0.1)
        return (Found == 1)

#------------------------------------------------------------

    def fix_generator(self, player, choice):
        """accepts generator pick from survivor"""
        if player not in self.gen_set[choice,:]:
            pos = self.gen_set[choice,:].index(0)
            self.gen_set[choice][pos] = player
        
        workOnGenerator = True

        skillCheck = np.random.binomial(1, 0.5)
        if skillCheck:
            popGenerator = np.random.binomial(1, 1/3)
            if popGenerator:
                decision = player.strategicMove("Pop")
                workOnGenerator = (decision == "Continue")

        if workOnGenerator:
            self.gen_vals[choice] += 1

        if self.gen_vals[choice] == 3:
            pos = self.gen_set[choice,:].index(0)
            self.gen_set[choice][pos] = 1
            self.gens_fixed += 1
            

#------------------------------------------------------------

    def hooked(self, players):
        pos = self.hook_set[:,0].index(players[1])
        killerCamping =  (self.hook_set[pos][1] != 0)
        
        decision = players[0].strategicMove("Save")
        if not killerCamping or decision == "Rescue":
            self.hook_set[pos][0] = 0
            self.free_survivors.append(players[1])
        else: return

        return self.chase(players)

#------------------------------------------------------------

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
                    i = random.randint(0,3)
                    self.hook_set[i][0] = chasedPlayer
                    self.free_survivors.remove(chasedPlayer)
                    chasedPlayer.hooks += 1
                    
                    if chasedPlayer.hooks == 3:
                        # KILL Player
                        self.dead_survivors.append(chasedPlayer)
                        self.hook_set[i][0] = 1
                        self.survivors_alive -= 1
                    else:    
                        camping = np.random.binomial(1, self.killer.camp_p)
                        if camping: 
                            self.hook_set[i][1] = self.killer
                            self.killer.busy = True
                    return

#------------------------------------------------------------


    def run_round(self):
        ''' Runs a single round of the game'''

        workingOnGen = self.gen_set[:,0]

        # Killers and free survivors take turns to play in a random order
        for player in random.shuffle(self.free_survivors.append(self.killer)):
            
            if self.survivors_alive == 1 and player != self.killer:
                TrapDoorFound = self.lookForTrapDoor(player)
                if TrapDoorFound: return ("Players won", player)

            if player in workingOnGen:
                scenario = ("Fix Gen", player, workingOnGen.index(player))
            else:           
                scenario = player.nextMove()

            if scenario[0] == "Chase":
                self.chase(scenario[1])
            elif scenario[0] == "Hooked":
                self.hooked(scenario[1])
            elif scenario[0] == "Fix Gen":
                self.fix_generator(scenario[1], scenario[2])
            else:
                continue

        if self.gens_fixed == 5:
            doorOpen = (self.canEscape == 0)
            if doorOpen: return ("Players Won", self.free_survivors)
            else: self.canEscape -= 1

        if self.survivors_alive == 0:
            return ("Game Over!", None)
        
        self.num_rounds += 1
        return
            
#------------------------------------------------------------


    def play(self):
        ''' Runs rounds until game is over '''
        Outcome = None
        while Outcome == None:
            Outcome = self.run_round()
        return self.payoff(Outcome)
            

#------------------------------------------------------------


    def payoff(self, Outcome):
        ''' Takes list of survivors alive and rewards everyone accordingly '''
        if Outcome[0] == "Game Over!":
            return
        else:
            winners = Outcome[1]
            numWinners = len(winners)

            for d in self.dead_survivors:
                d.score += 0.5 * d.score
            for w in winners:
                w.score += numWinners * w.score
                
        