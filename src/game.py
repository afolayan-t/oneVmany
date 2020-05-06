import numpy as np
import random
import player_classes

def column(matrix, i):
    return [row[i] for row in matrix]

class dbd:
    """Defines state of game"""
   
    def __init__(self, killer, survivors):
        self.gen_set = np.zeros((7,3), dtype=player_classes.survivor) # 0 if not in use, 1 if fixed, player_object if being worked on
        self.gen_vals = np.zeros((7)) # 0 if not fixed, 3 if fixed
        self.hook_set = np.zeros((4,2), dtype=player_classes.survivor) # 0 if not in use, 1 if used, player_object if hooked
        self.trap_door_open = False 

        self.num_rounds = 0
        self.survivors = [survivors[0], survivors[1], survivors[2], survivors[3]]
        self.free_survivors = survivors
        self.dead_survivors = []
        self.killer = killer

        self.survivors_alive = 4
        self.gens_fixed = 0
        self.canEscape = 2 # After all generators fixed, players must wait 2 rounds before being able to escape

#------------------------------------------------------------

    
    def __repr__(self):
        print("Round Number: " + self.num_rounds)
        print("Survivors Alive: " + self.survivors_alive)
        print("Generators Fixed: " + self.gens_fixed)

#------------------------------------------------------------

    def lookForTrapDoor(self, player):
        Found = np.random.binomial(1, 0.1)
        if Found:
            player.score += 50
        player.r = min(.9,player.r+.1)
        return (Found == 1)

#------------------------------------------------------------

    def fix_generator(self, player, choice):
        """accepts generator pick from survivor"""
        if player not in self.gen_set[choice]:
            pos = np.where(self.gen_set[choice] == 0)[0]
            if len(pos) == 0: return
            pos = pos[0]
            self.gen_set[choice][pos] = player

        
        workOnGenerator = True

        skillCheck = np.random.binomial(1, 0.5)
        if skillCheck:
            popGenerator = np.random.binomial(1, 1/3)
            if popGenerator:
                decision = player.strategicMove("Pop")
                workOnGenerator = (decision == "Continue")
                if workOnGenerator:
                    player.r = min(.9,player.r+.3)
                else:
                    pos = np.where(self.gen_set[choice] == player)
                    self.gen_set[choice][pos] = 0
                    return

        if workOnGenerator:
            self.gen_vals[choice] += 1

        if self.gen_vals[choice] == 5:
            self.gens_fixed += 1
            p=self.gen_set[choice,:]
            for i in range(len(p)):
                if p[i]!=0:
                    p[i].score+=10
                self.gen_set[choice][i] = 1

#------------------------------------------------------------

    def hooked(self, players):
        pos = np.where(self.hook_set[:,0] == players[1])[0][0]
        killerCamping =  all([self.hook_set[pos][1] != 0, self.hook_set[pos][1] != 1])
        
        decision = players[0].strategicMove("Save")
        if not killerCamping or decision == "Rescue":
            self.hook_set[pos][0] = 0
            self.free_survivors.append(players[1])
            players[0].score += 25
            players[0].r = min(.9, players[0].r + .3)
            
        else: return

        self.killer.busy = False
        self.hook_set[pos][1] = 0

        return self.chase(players)

#------------------------------------------------------------

    def chase(self, players):


        chasedPlayers = players 

        numChased = len(players)

        if numChased == 1:
            probs = {"Obstacle": 0.3, "Stun": 0.05, "Run": 0.2}
        else:
            probs_1 = {"Obstacle": 0.8, "Stun": 0.2, "Run": 0.5}
            probs_2 = {"Obstacle": 0.3, "Stun": 0.9, "Run": 0.5}
        
        
        turn = 0
        for chasedPlayer in chasedPlayers:
            
            
            if turn == 0 and numChased > 1:
                probs = probs_1
            if turn == 1 and numChased > 1:
                probs = probs_2
            
            while(True): 

                playerStrat = chasedPlayer.strategicMove("Chased")
                chaseOutcome = np.random.binomial(1, probs[playerStrat])

                if chaseOutcome == 1: # Escaped
                    chasedPlayer.score += 30
                    break
                else:  # Hit by killer
                    if not chasedPlayer.is_injured: # First hit -> continue chase
                        chasedPlayer.is_injured = True
                        chasedPlayer.r = min(.9, chasedPlayer.r+.3)
                    else: 
                        i = random.randint(0,3)
                        self.hook_set[i][0] = chasedPlayer                        
                        for p in self.free_survivors:
                            if p == chasedPlayer: self.free_survivors.remove(p)

                        chasedPlayer.hooks += 1
                        
                        if chasedPlayer.hooks == 3:
                            # KILL Player
                            self.dead_survivors.append(chasedPlayer)
                            self.hook_set[i][0] = 1
                            self.hook_set[i][1] = 1
                            self.survivors_alive -= 1
                        else:    
                            camping = np.random.binomial(1, self.killer.camp_p)
                            if camping: 
                                self.hook_set[i][1] = self.killer
                                self.killer.busy = True
            turn=1


#------------------------------------------------------------


    def run_round(self):
        ''' Runs a single round of the game'''

        workingOnGen = column(self.gen_set, 0) + column(self.gen_set, 1) + column(self.gen_set, 2)
        

        # Killers and free survivors take turns to play in a random order
        avail_players = self.free_survivors + [self.killer]
        random.shuffle(avail_players)
        for player in avail_players:
            
            if self.survivors_alive == 1 and player != self.killer:
                TrapDoorFound = self.lookForTrapDoor(player)
                if TrapDoorFound: return ("Players won", [player])

            if player in workingOnGen:
                scenario = ("Fix Gen", player, workingOnGen.index(player) % 7)
            else:           
                scenario = player.nextMove(self)

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
        for survivor in self.free_survivors:
            survivor.r = max(0.1,survivor.r-.1)

        return None
            
#------------------------------------------------------------


    def play(self):
        ''' Runs rounds until game is over '''
        Outcome = None
        while Outcome == None:
            Outcome = self.run_round()
            if self.num_rounds == 100: 
                return True
        self.payoff(Outcome)
        return False
            

#------------------------------------------------------------


    def payoff(self, Outcome):
        ''' Takes list of survivors alive and rewards everyone accordingly '''
        print(Outcome[0])
        if Outcome[0] == "Game Over!":
            return
        else:
            winners = Outcome[1]
            numWinners = len(winners)

            for d in self.dead_survivors:
                d.score += 0.5 * d.score
            for w in winners:
                w.score += numWinners * w.score
                
        
