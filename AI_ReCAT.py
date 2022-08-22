"""
For the given below-board game, help the Blue Triangular coin which is located at (1,3) to reach the Red Circle coin in (6,4) via the optimal path (shortest one) using the BFS algorithm.
The possible actions of the coin to move around the cells on the board are {Left, Right, Up, Down}.
The coin can’t move into shaded cells to expand the nodes further.
Also, the coin can’t cross the four side boundaries. Use (Row, Column) format to represent each cell.
The dimension of the the board is 6x6.
Calculate the space and time complexity of the algorithm for the given scenario.
Draw the search tree to validate the output generated by the program.
Write an algorithm with input and output

"""


import sys
import time

# shaded regions to avoid = 1
# coin = (1, 3)
# triangle = (6,4)
#


board = [
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]


# function to define the Action
def Actions(board, state):
    # define the actions
    actions = []
    # check if the state is in the board
    if (
        state[0] >= 0
        and state[0] < len(board)
        and state[1] >= 0
        and state[1] < len(board[0])
    ):
        # check if the state is not shaded
        if board[state[0]][state[1]] == 0:
            # check if the state is not the start state
            if state != (1, 3):
                # check if the state is not the end state
                if state != (6, 4):
                    actions.append((state[0], state[1] - 1))
                    actions.append((state[0], state[1] + 1))
                    actions.append((state[0] - 1, state[1]))
                    actions.append((state[0] + 1, state[1]))
    return actions


def BFS(board, start, end):
    # define the queue
    queue = []
    # define the visited
    visited = []
    # define the path
    path = []
    # define the current state
    current = start
    # define the parent
    parent = {}
    # define the cost
    cost = {}
    # define the cost
    cost[start] = 0
    # define the parent
    parent[start] = None
    # define the visited
    visited.append(start)
    # define the queue
    queue.append(start)
    # define the path
    path.append(start)
    # define the current state
    current = start
    # define the parent
    parent[start] = None
    # define the cost
    cost[start] = 0
    # define the cost
    cost[start] = 0
    # define the parent
    parent[start] = None
    # define the visited
    visited.append(start)
    # define the queue
    queue.append(start)
    # define the path
    path.append(start)
    # define the current state
    current = start
    # define the parent
    parent[start] = None
    # define the cost
    cost[start] = 0
    # define the cost
    cost[start] = 0
    # define the parent
    parent[start] = None
    # define the visited
    visited.append(start)
    # define the queue
    queue.append(start)
    # define the path
    path.append(start)
    # define the current state
    current = start
    # define the parent
    parent[start] = None
    # define the cost
    cost[start] = 0
    # define the cost
    cost[start] = 0
    # define the parent
    parent[start] = None
    # define the visited
    visited.append(start)
    # define the queue
    queue.append(start)
    # define the path
    path.append(start)
    # define the current state
    current = start
    # define the parent
    parent[start] = None


def main():
    start = (1, 3)
    end = (6, 4)
    print("BFS: ", BFS(board, start, end))