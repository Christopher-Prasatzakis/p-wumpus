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
from sys import exit

# The game grid.
grid = [[' ' for _ in range(20)] for _ in range(10)]

# The position of the player at any given time.
player_x = 0
player_y = 0

# The number of rounds the player has in their rifle.
rounds = 5

# Let's also make the number of wumpi global...
n_wumpi = 1

# What to do in a Game Over situation.
def game_over():
    print("\nGame Over\n")
    
    # Let the player decide.
    inp = input("Do you want to (R)estart or (Q)uit? ")[0]
    
    while (inp not in "qQrR"):
        inp = input("Do you want to (R)estart or (Q)uit? ")[0]
        
    if (inp.upper() == 'Q'):
        exit()
    else:
        print("Let's play again, then!")
        initialize()

# Routine that evaluates a command given by the player.
def command_eval(command):
    global player_x, player_y, rounds, n_wumpi
    
    directions = ["NORTH", "EAST", "WEST", "SOUTH"]
    directions_short = "NEWS"
    fires = ["FIRE NORTH", "FIRE EAST", "FIRE WEST", "FIRE SOUTH"]
    fires_short = ["FIRE N", "FIRE E", "FIRE W", "FIRE S"]
    
    # Capitalize user input.
    command_r = command.upper()
    
    # Evaluate direction commands first.
    if ((command_r in directions) or (command_r in directions_short)):
        x = player_x
        y = player_y
        
        # Calculate new player position.
        if (command_r[0] == "N"):
            y = y - 1
        elif (command_r[0] == "E"):
            x = x + 1
        elif (command_r[0] == "W"):
            x = x - 1
        elif (command_r[0] == "S"):
            y = y + 1
            
        # Examine the scenarios where a move is either illegal
        # or results in a Game Over.
        if (((x < 0) or (x > 19)) or ((y < 0) or (y > 9))):
            print("Can't go that way, sorry.")
        else:
            if (grid[y][x] == 'W'):
                print("You were eaten by a Wumpus. Too bad!")
                game_over()
            elif (grid[y][x] == 'F'):
                print("You fell into a pitfall to your death.")
                game_over()
            elif (grid[y][x] == 'G'):
                print("You found the treasure! Yaaaaaaaaaaay!!!")
                game_over()
            else:
                grid[y][x] = 'P'
                grid[player_y][player_x] = ' '
                player_y = y
                player_x = x
    elif ((command_r in fires) or (command_r in fires_short)):
        # First of all, can the rifle fire?
        if (rounds == 0):
            print("Your rifle is out of ammunition.")
        else:
            # For firing, get the firing direction.
            firing_direction = command_r.split()[1]
        
            # Where should the bullet go?
            x = player_x
            y = player_y
        
            if (firing_direction[0] == "N"):
                y = y - 1
            elif (firing_direction[0] == "E"):
                x = x + 1
            elif (firing_direction[0] == "W"):
                x = x - 1
            elif (firing_direction[0] == "S"):
                y = y + 1
                
            if (y < 0): y = 0
            if (y > 9): y = 9
            if (x < 0): x = 0
            if (x > 19): x = 19
            
            # Did the bullet hit a Wumpus?
            if (grid[y][x] == 'W'):
                print("You hear a beastly scream and a death rattle...")
                n_wumpi = n_wumpi - 1
                grid[y][x] = ' '
                print(f"There are now {n_wumpi} Wumpi remaining...")
            else:
                print("You fire your rifle into thin air...")
                
            rounds = rounds - 1
            print(f"Your rifle has now {rounds} rounds remaining...")
    elif (command_r == "RESTART"):
        inp = input("Do you want to restart the game (Y/N)? ")[0]
        inp = inp.upper()
        
        if (inp == 'Y'):
            print("\nRestarting...")
            initialize()
    elif (command_r == "QUIT"):
        inp = input("Do you want to quit (Y/N)? ")[0]
        inp = inp.upper()
        
        if (inp == 'Y'):
            print("\nThank you for playing P-Wumpus!")
            exit()
    else:
        print("I did not recognize this command.")

# Routine that evaluates the squares surrounding the player character.
def surrounding_eval():
    # Make list of surrounding squares to be evaluated.
    squares = []
    
    if (player_y > 0):
        squares.append((player_x, player_y - 1, "north"))
        
    if (player_y < 9):
        squares.append((player_x, player_y + 1, "south"))
        
    if (player_x < 19):
        squares.append((player_x + 1, player_y, "east"))
        
    if (player_x > 0):
        squares.append((player_x - 1, player_y, "west"))
        
    # Evaluate the adjacent squares.
    for square in squares:
        square_x = square[0]
        square_y = square[1]
        direction = square[2]
        
        if (grid[square_y][square_x] == 'W'):
            print(f"You smell something horrible to the {direction}...")
        elif (grid[square_y][square_x] == 'G'):
            print(f"You see something glittering to the {direction}...")
        elif (grid[square_y][square_x] == 'F'):
            print(f"You feel a breeze coming from the {direction}...")

# The main game loop.
def play():
    while (True):
        # Check the player's surroundings first.
        surrounding_eval()
        
        # Await player input.
        command = input("> ")
        
        # Process player input.
        command_eval(command)
        
# Generate a random level and start the game.
def initialize():
    global n_wumpi, player_x, player_y, rounds, grid
    
    seed(time()) # Randomize timer.
    
    grid = [[' ' for _ in range(20)] for _ in range(10)] # Initialize grid.
    
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
    
    # The player starts off with 5 rounds in their rifle.
    rounds = 5
    
    # Start the game!
    play()
    
# The main function.
def main():
    print("P-Wumpus  Copyright (C) 2026 Christopher Prasatzakis")
    print("This program comes with ABSOLUTELY NO WARRANTY;")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions; see LICENSE for details.\n")
    print("New game starting...\n")
    initialize()
    
main()
