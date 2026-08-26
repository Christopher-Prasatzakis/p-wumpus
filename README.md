# p-wumpus
This little Python 3 game is a take on the Wumpus World concept (https://en.wikipedia.org/wiki/Wumpus_world), taking place in a 20x10 grid.

You start off with a rifle containing only five rounds. Your mission is simple: get the treasure while avoiding being eaten by the Wumpi or falling into a pitfall.

Good luck, adventurer. You will need it.

## Playing the game
Running the game is pretty easy and can be done in three simple steps:

1) Install Python (https://www.python.org/)
2) Run pwumpus.py with this command on a terminal: python3 pwumpus.py
3) Enjoy!

This is a text adventure-style game. You play it by entering commands in a command prompt. These are the commands you can use:

1) n(orth), s(outh), w(est) and e(ast): Move to the respective square adjacent to the one your player character is (you always start at square (0, 0) - the top left of the grid).
2) fire <n(orth), s(outh), e(ast), w(est)>: Fire your rifle at that square adjacent to yours. If there is a Wumpus there, it kills it.
3) restart: Restart the game. Useful in the event something breaks or you find yourself in an unwinnable position.
4) quit: Self-explainatory.

## Licensing information
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License  (LICENSE) for more details.
