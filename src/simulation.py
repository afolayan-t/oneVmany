import game
import random
import player_classes
import matplotlib.pyplot as plt


# Available startegies
STRATEGIES = ["SELFLESS", "SELFISH", "SELFLESS-LEANING", "SELFISH-LEANING", "STANDARD"]

stratScores = {"SELFLESS":[], "SELFISH":[], "SELFLESS-LEANING":[], "SELFISH-LEANING":[], "STANDARD":[]}
stratNumEscapes = {"SELFLESS":0, "SELFISH":0, "SELFLESS-LEANING":0, "SELFISH-LEANING":0, "STANDARD":0}


# Defines how players for each strtagey we will have for a particular game
playerSET = [[4, 0, 0, 0, 0],    # i.e. 4 SELFLESS players
             [0, 4, 0, 0, 0],
             [0, 0, 4, 0, 0],
             [0, 0, 0, 4, 0],
             [0, 0, 0, 0, 4],
             [1, 1, 1, 1, 1],   # One of them sits out each round
             [3, 1, 0, 0, 0],
             [1, 3, 0, 0, 0],
             [0, 0, 1, 3, 0],
             [0, 0, 3, 1, 0],
             [2, 2, 0, 0, 0],
             [0, 0, 2, 2, 0]]

TotalGamesPlayed = 0
print("Begin Games")
for playerDist in playerSET:
    
    print("================================================")
    # Initialize players
    ps = []
    playerNum = 1
    whosPlaying = "Players playing "
    for i in range(len(playerDist)):
        for j in range(playerDist[i]):
            playerName = "P" + str(playerNum)
            playerStrategy = STRATEGIES[i]
            ps.append(player_classes.survivor(playerName, playerStrategy))
            playerNum += 1
            whosPlaying += playerName + ":" + playerStrategy + " "

    print(whosPlaying)
    print("----------------------------------------")
    #exit()

    K = player_classes.killer()

    # Play 100 games of each player set
    for game_num in range(100):

        # If all strategies playing (5), make one sit out each game 
        if len(ps) > 4:
            playerSittingOut = game_num % 5 
            survivorPlayers = [ps[i] for i in range(len(ps)) if i != playerSittingOut]
        else:
            survivorPlayers = [ps[0], ps[1], ps[2], ps[3]]
        
        # Create new game and play through till the end
        match = game.dbd(K, survivorPlayers)
        Outcome = match.play()
        
        # Game stuck in infinite loop for some reason
        if Outcome == None: continue

        # Find out who survived based on outcome and Update their escape values
        final = Outcome[0]
        if final == "Game Over!":
            final += " No survivors"
        else:
            for p in Outcome[1]:
                final += " " + p.player_name
                stratNumEscapes[p.player_strategy] += 1 # Update num escapes for strategy
            final += " Escaped!"

        print(final)
    
        # Save scores and reset all players
        for p in match.players:
            stratScores[p.player_strategy].append(p.score)
            p.reset()
        
        TotalGamesPlayed +=1

        

print(stratNumEscapes)
print(stratScores)


#plt.plot(playerHistory[0], playerHistory[1], playerHistory[2], playerHistory[3])
#plt.show()


