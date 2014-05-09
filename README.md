Game_of_Life
============
First, make sure to Install matplotlib---python plotting library

Second, to run from the main folder "Game_of_Life" use the following command to see the animation:

$python bin/simple_game_of_life.py


---Description:

This is a simple game called game of life in 2 dimensional grid world. First the each
tile of the grid is represented by a 0 number indicating the cell is dead and non-zero number
indicating it is alive. Each cell is 8 neighbors up, down, right, left and diagonal ones.... If the cell is
in the bourder we assume the world the periodic so it considers the neigbor on the opposite side of the
border.

The rules are as follows:

rule 1: if the cell is live then is does dies "under populated"  if total neighbor live cells = {1,0}
rule 2: if live lives if total neighbor live cells  = {2,3}
rule 3: if live, dies if total  neighbor live cells =  {4,5,6}
rule 4: if dead, lives if total  neighbor live cells =  {3}

Given the current configuation (Grid world state) check the current status (live or not live) and make a transition
to the new state

This is demonstrates in the form of animation using numpy library
