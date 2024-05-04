# [CS 170] Eight-Puzzle-Project
Project 1: Solve the Eight Puzzle Problem

Problem: 

The Eight Puzzle consists of a 3x3 board with 8 numbered tiles and one blank space. The goal is to move the tiles around until the blank space in the bottom-right corner.


Approach 1: 

We will be using the Uniform Cost Search method.

1) Uniform Cost Search Overview

- Uniform Cost Search expands the node with the lowest path cost g(n) at each step.
- It is essentially a breadth-first search that uses a priority queue to find the least expensive path.
    - We will keep a closed list of expanded nodes to avoid revisiting the same state.

2) Cost Function

- g(n): the actual cost from the start node to any node n. 
    - This can be considered as the number of moves made from the initial state to reach the current state.
- h(n): hardcoded to zero because Uniform Cost Search does not use heuristic function.
- f(n) = g(n): It represents the estimated total cost of the cheapest solution through n.

3) Algorithm

- Initialize the priority open list with the initial state of the puzzle, with a path cost of 0.
- Loop until the open list is empty:
    - Remove the node with the lowest g(n) from the open list.
    - Generate all its successors by moving the blank space up, down, left, or right.
    - For each successor:
        - Calculate g(n) for the successor as the parent's g(n) plus the cost of the move (1 for each move in our case).
        - If it is the goal, stop and return the solution by tracing the path back to the initial state.
        - If a node with the same position as the successor is in the open list but has a higher g(n), replace it with the new lower-cost node.
        - Otherwise, add the successor to the open list if it is not already present with a lower cost.
- Return Fail if no solution is found after the open list is exhausted.

4) Optimization 

- Cycle Checking: Keep a closed list of expanded nodes to avoid revisiting the same state. 
    - We can add each explored node to a list and check this list each time we want to add a node to the open list.
- Path Reconstruction: Maintain a parent link in each node to trace back the solution path once the goal state is found.

Approach 2: 

We will be using the A* with the Misplaced Tile heuristic method.

1) 


Approach 3: 

We will be using the A* with the Euclidean Distance heuristic method.

1) A* with the Euclidean Distance heuristic method overview

- A* algorithm is a search algorithm that is used to find the shortest path from a start node to a target node

2) Cost Function

- g(n): the actual cost from the start node to any node n.
- h(n): a heuristic that estimates the cost of the cheapest path from n to the goal. 
    - h(n) = sqrt[(x2​−x1​)^2 + (y2​−y1​)^2​]
- f(n) = g(n) + h(n): the cost function that A* minimizes. It represents the estimated total cost of the cheapest solution through n.

3) Choosing the Heuristic [h(n)]

- The heuristic function estimates the minimum cost from the current state to the goal state. 
- The Euclidean Distance heuristic measures the straight-line distance between each tile’s current position and its goal position, summing these distances across all tiles. It's calculated as follows:
    - h(n) = sqrt[(x2​−x1​)^2 + (y2​−y1​)^2​]
        - (x1, y1) is the current position of a tile, and (x2, y2) is the position in the goal state.

4) Algorithm

- Initialize the open list (priority queue) with the initial state of the puzzle.
- Loop until the open list is empty:
    - Remove the node with the lowest f(n) from the open list.
    - Generate all its successors by moving the blank space up, down, left, or right
    - For each successor:
        - Compute g, h, and f (cost functions)
        - If it is the goal, stop and return the solution by tracing the path back to the initial state.
        - If a node with the same position as successor is in the open list with lower f, skip this successor.
        - Otherwise, add the successor to the open list.
- Return Fail if no solution is found after the open list is exhausted.











**Imports:**

* `heapq`: This module provides functions for implementing priority queues, which are essential for A* search.
* `math`: This module provides mathematical functions, used here to calculate the Euclidean distance heuristic.

**Classes:**

* **Problem:**
    * This class represents the 8-puzzle problem itself.
    * It takes two arguments:
        * `initial`: The starting configuration of the puzzle tiles (a list of numbers).
        * `goal` (optional): The goal configuration of the puzzle tiles (defaults to a solved state: [1, 2, 3, 4, 5, 6, 7, 8, 0]).
    * It stores the `initial_state` and `goal_state` as attributes.
    * It also defines a list `operators` representing the possible moves (up, down, left, right) as offsets to be applied to the tile positions.

* **PuzzleState:**
    * This class represents a single state of the puzzle during the search.
    * It takes six arguments:
        * `configuration`: The current configuration of the puzzle tiles (a list of numbers).
        * `problem`: A reference to the problem instance.
        * `parent` (optional): The parent state in the search path (used for backtracking).
        * `move` (optional): The move made to reach this state from the parent (useful for debugging).
        * `cost`: The cost of reaching this state from the initial state (typically the number of moves made).
    * It stores all the provided arguments as attributes.
    * It also defines additional attributes:
        * `blank_pos`: The index of the blank tile in the current configuration (found by calling `find_blank`).
        * `heuristic`: The heuristic score of the state, calculated using the `euclidean_distance` method.
        * `score`: The total score f(n) of the state, which is the sum of `cost` and `heuristic`.
    * Methods:
        * `find_blank`: Finds the index of the blank tile in the configuration.
        * `euclidean_distance`: Calculates the Euclidean distance heuristic. This heuristic estimates the remaining distance to the goal state by summing the Euclidean distances of each misplaced tile from its goal position. 
        * `generate_children`: Generates all possible child states by applying the defined operators (moving the blank tile) and creating new `PuzzleState` instances for each valid child.
        * `is_goal`: Checks if the current configuration matches the goal configuration.
        * `__lt__`: This method defines the comparison behavior for the priority queue. It sorts states based on their total score (f(n)) for A* search.

**Function:**

* **a_star(problem):**
    * This function implements the A* search algorithm to solve the 8-puzzle problem.
    * It takes a `problem` instance as input.
    * Here's what it does:
        1. Initializes:
            * Creates an initial state object (`initial_state`) from the problem's initial configuration.
            * Creates an empty priority queue (`open_list`) to store states to be explored. The queue is implemented using `heapq` for efficient retrieval of the state with the lowest f(n) score.
            * Creates a set (`visited`) to track visited configurations and prevent revisiting them.
        2. Main loop:
            * While the `open_list` is not empty:
                * Dequeue the state with the lowest f(n) score from the `open_list` using `heapq.heappop`. This is the most promising state to explore next.
                * If the dequeued state is the goal state (as determined by `is_goal`), the search is successful. The function returns the goal state, which can be used to backtrack and reconstruct the solution path.
                * Otherwise, generate all child states of the current state using `generate_children`.
                * For each child state:
                    * Convert the child's configuration to a tuple for efficient hashing.
                    * If the child's configuration hasn't been visited before (check using `visited`), add it to the `visited` set and the `open_list` priority queue.
        3. If the loop exits without finding the goal state, it means no solution exists, and the function returns `None`.


