import heapq  # Importing heapq for priority queue support.
import math


class Problem:
    # Initialize the problem with the initial state and an optional goal state.
    def __init__(self, initial, goal=None):

        # The starting configuration of the puzzle.
        self.initial_state = initial  

        # Default goal state.
        self.goal_state = goal if goal else [1, 2, 3, 4, 5, 6, 7, 8, 0]  

         # Possible moves: up, down, left, right.
        self.operators = [(-1, 0), (1, 0), (0, -1), (0, 1)] 


class PuzzleState:

    # Initialize the puzzle state within the context of a problem.
    def __init__(self, configuration, problem, parent=None, move=None, cost=0):
       
        self.configuration = configuration  # Current tile configuration.
        self.problem = problem  # Reference to the problem instance.
        self.parent = parent  # Reference to the parent state in the search path.
        self.move = move  # The move made to reach this state from the parent.
        self.cost = cost  # The cost from the initial state to this state.
        self.blank_pos = self.find_blank()  # Location of the blank tile.
        self.heuristic = self.misplaced_tile_heuristic()  # Compute the misplaced tile heuristic.
        self.score = self.cost + self.heuristic  # Total score f(n) = g(n) + h(n).
        
    def find_blank(self): 
        # Return index of blank tile
        return self.configuration.index(0)
    
    def expand_nodes(self):
        frontier = [] # Setup frontier
        
     
    # Check if the current configuration matches the goal configuration.
    def is_goal(self):
        return self.configuration == self.problem.goal_state

def misplaced_tile_heuristic(self):
        misplaced_tile_count = 0
        # Loop through initial state, count number of misplaced tiles against goal state
        for i in range(9):
            if (self.configuration[i] != 0) and (self.configuration[i] != self.problem.goal_state[i]):
                misplaced_tile_count += 1
        return misplaced_tile_count
