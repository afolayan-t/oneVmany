import game
import random
import player_classes
import matplotlib.pyplot as plt

playerHistory = [[] for x in range(5)]

# Play 1000 games
for game_num in range(10):

    # Initial Players
    p1 = player_classes.survivor("P1", "SELFLESS")
    p2 = player_classes.survivor("P2", "SELFISH")
    p3 = player_classes.survivor("P3", "SELFLESS-LEANING")
    p4 = player_classes.survivor("P4", "STANDARD")
    p5 = player_classes.survivor("P5", "SELFISH-LEANING")
    ps = [p1, p2, p3, p4, p5]

    K = player_classes.killer()

    # Create new game and play through till the end
    random.shuffle(ps)
    survivorPlayers = ps[:-1]
    match = game.dbd(K, survivorPlayers)
    gameStuck = match.play()
    
    if gameStuck: continue

    # Save and reset player scores
    for p in match.survivors:
        idx = int(p.player_name[1]) - 1
        playerHistory[idx].append( p.score)

playerHistory = [ls for ls in playerHistory if len(ls) > 0]
print(playerHistory)


#plt.plot(playerHistory[0], playerHistory[1], playerHistory[2], playerHistory[3])
#plt.show()


