import game
import player_classes
import matplotlib as plt

playerHistory = [[] for x in range(4)]

p1 = player_classes.survivor("P1", "SELFLESS")
p2 = player_classes.survivor("P2", "SELFISH")
p3 = player_classes.survivor("P3", "TRUST")
p4 = player_classes.survivor("P4", "RANDOM")
ps = [p1, p2, p3, p4]

K = player_classes.killer()

# Play 1000 games
for game_num in range(1000):
    
    # Create new game and play through till the end
    game = game.dbd(K, ps)
    game.play()

    # Save and reset player scores
    for i in range(len(ps)):
        prevScore = playerHistory[i][-1]
        newScore = ps[i].score
        playerHistory[i].append( prevScore + newScore )
        ps[i].score = 0
    
    




