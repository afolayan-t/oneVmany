# Best Strategies in Repeated One Vs. Many games: Dead by Daylight


## Abstract

The One Vs. Many archetypes are one that shows up in many interactions in modern society. Examples being Parents vs. their children, Employees Vs. Employers, Teacher Vs. Student and Large distributors Vs. Small Business. In an effort to study a formulation of One Vs. Many formats, a simulation was created to encapsulate a particular One Vs. Many games, called Dead by Daylight,  through N-person Extensive Game Decisions Tree.  Dead by Daylight is a One Vs. Many games where a single Killer hunts four survivors who are trying to escape. The decision trees that define this game simulate different scenarios in the game, and different players' action sets within the game. We define five player strategies and pit them against each other in repeated games. In the end, there didn't seem to be a strategy that generally outperformed the rest. The One Vs. Many Scenarios are particularly interesting because of the way it mimics the betray and cooperation group interplay of modern everyday life. 

## Code

_**Breakdown**_

Our code consists of three python files,

       - player_classses: Consists of the Survivor and Killer object classes
       - game: Consists of the DBD game object class
       - simulation: Runs simulations of the DBD game on different player strategies and records data to be analyzed
       
 _**Running Games**_
 
 To run the games, you just need to run the simulation file with python3,
 
 ```
 $ python3 simulation.py
 ```
 
 This will cause the script to start printing game information regarding what kind of players are playing the current game, and what the final outcome was. Data regarding the different strategies' scores and number of wins is recorded across all games and plotted. 
 
 Note the code for the plots is only in the DBD.ipynb (jupyter notebook) file as it tends to display plots more elegantly than just running the code through terminal. 






                

