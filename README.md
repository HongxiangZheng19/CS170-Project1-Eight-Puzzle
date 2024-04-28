# [CS 170] Eight-Puzzle-Project
Project 1: Solve the Eight Puzzle Problem

* Problem: 
The Eight Puzzle consists of a 3x3 board with 8 numbered tiles and one blank space. The goal is to move the tiles around until they are in order, usually with the blank space in the bottom-right corner.


* Approach: 
We will be using the A* with the Euclidean Distance heuristic method.

1) A* algorithm is a search algorithm that is used to find the shortest path from a start node to a target node

- g(n): the actual cost from the start node to any node n.
- h(n): a heuristic that estimates the cost of the cheapest path from n to the goal. 
- f(n) = g(n) + h(n): the cost function that A* minimizes. It represents the estimated total cost of the cheapest solution through n.

2) Choosing the Heuristic [h(n)]

- The heuristic function estimates the minimum cost from the current state to the goal state. 
- The Euclidean Distance heuristic measures the straight-line distance between each tile’s current position and its goal position, summing these distances across all tiles. It's calculated as follows:
    - h(n) = sqrt[(x2​−x1​)^2+(y2​−y1​)^2​)]
        - (x1, y1) is the current position of a tile, and (x2, y2) is the position in the goal state.

3) Execution

- Initialize the open list (priority queue) with the initial state of the puzzle.
- Loop until the open list is empty:
    - Remove the node with the lowest f(n) from the open list.
    - Generate all its successors by moving the blank space up, down, left, or right
    - Compute g, h, and f for each successor.
    - For each successor:
        - If it is the goal, stop and return the solution by tracing the path back to the initial state.
        - If a node with the same position as successor is in the open list with lower f, skip adding this successor.
        - Otherwise, add the successor to the open list.
- Return failure if no solution is found after the open list is exhausted.

4) Optimization

- Cycle checking: Keep a closed list of expanded nodes to avoid revisiting the same state.