"""
P-Wumpus: The "Wumpus World" game remade in Python3
Copyright (C) 2026 Christopher Prasatzakis

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Both of these are imported for random level generation.
from time import time
from random import seed
from random import randint

# The game grid.
grid = [[' ' for _ in range(20)] for _ in range(10)]

# The position of the player at any given time.
player_x = 0
player_y = 0

# Generate a random level and start the game.
def initialize():
    seed(time()) # Randomize timer.
    
    n_wumpi = randint(1, 5) # How many wumpi will there be?
    
    n_pitfalls = randint(0, 10) # Ditto for pitfalls.
    
    # Add the wumpi to the grid. All in separate squares and
    # away from the starting square, please!
    i = 0
    
    while (i < n_wumpi):
        wumpus_x = randint(0, 19)
        wumpus_y = randint(0, 9)
        
        if ((wumpus_x == 0) and (wumpus_y == 0)):
            continue
            
        if (grid[wumpus_y][wumpus_x] != ' '):
            continue
            
        grid[wumpus_y][wumpus_x] = 'W'
        
        i = i + 1
        
    # Ditto for the pitfalls.
    i = 0
    
    while (i < n_pitfalls):
        pitfall_x = randint(0, 19)
        pitfall_y = randint(0, 9)
        
        if ((pitfall_x == 0) and (pitfall_y == 0)):
            continue
            
        if (grid[pitfall_y][pitfall_x] != ' '):
            continue
            
        grid[pitfall_y][pitfall_x] = 'F'
        
        i = i + 1
        
    # And now, place the treasure.
    treasure_x = randint(0, 19)
    treasure_y = randint(0, 9)
    
    while (grid[treasure_y][treasure_x] != ' '):
        treasure_x = randint(0, 19)
        treasure_y = randint(0, 9)
        
    grid[treasure_y][treasure_x] = 'G'
    
    # Place the player at the topmost left square (0, 0)
    grid[0][0] = 'P'
    player_x = player_y = 0
    
    # Start the game!
    #play()
