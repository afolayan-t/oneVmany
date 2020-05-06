import game.py
import player_classes.py
import matplotlib.pyplot as plt

playerHistory = [[] for x in range(4)]

p1 = player_classes.survivor("P1", "SELFLESS")
p2 = player_classes.survivor("P2", "SELFISH")
p3 = player_classes.survivor("P3", "SELFLESS-LEANING")
p4 = player_classes.survivor("P4", "STANDARD")
p5 = player_classes.survivor("P5", "SELFISH-LEANING")
ps = [p1, p2, p3, p4, p6]

K = player_classes.killer()

# Play 1000 games
for game_num in range(1):
    
    # Create new game and play through till the end
    players = random.shuffle(ps)
    game = game.dbd(K, ps[:-1])
    game.play()

    # Save and reset player scores
    for i in range(len(ps)):
        prevScore = playerHistory[i][-1]
        newScore = ps[i].score
        playerHistory[i].append( prevScore + newScore )
        ps[i].score = 0
    

plt.plot(playerHistory[0], playerHistory[1], playerHistory[2], playerHistory[3])
plt.show()


