"""
For the given below-board game, help the Blue Triangular coin which is located at (2,5) to reach the Red Circle coin in (6,3) using A* algorithm with maximum path cost i.e., a path with maximum points.
The possible actions of the coin to move around the cells on the board are {Left, Right, Up, Down}. The coin can’t move into shaded cells to expand the nodes further. Also, the coin can’t cross the four side boundaries. 
Use (Row, Column) format to represent each cell. Each cell is associated with points. 

"""

import networkx
