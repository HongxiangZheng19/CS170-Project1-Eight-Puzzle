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
    
    def misplaced_tile_heuristic(self):
        misplaced_tile_count = 0
        # Loop through initial state, count number of misplaced tiles against goal state
        for i in range(9):
            if (self.configuration[i] != 0) and (self.configuration[i] != self.problem.goal_state[i]):
                misplaced_tile_count += 1
        return misplaced_tile_count
    
    def generate_children(self):
        children = []
        blank_pos = self.find_blank
        y, x = divmod(blank_pos, 3) # locate the blank, turn it into x, y coords 
        for dx,dy in self.problem.operator: # Check blank tile's up/down/left/right
            nx, ny = x + dx, y + dy #  create x,y coords of all possible moves
            blank_after_swap = nx * 3 + ny # new position of blank tile after moves are initiated
            new_config = self.configuration # copy parent config
            new_config[blank_pos], new_config[blank_after_swap] = new_config[blank_after_swap], new_config[blank_pos]
            children.append(PuzzleState(self, new_config, new_config.problem, parent = self.configuration, move = blank_after_swap, cost = self.cost + 1))
        return children
     
    # Check if the current configuration matches the goal configuration.
    def is_goal(self):
        return self.configuration == self.problem.goal_state
    
    def a_star(problem):
        initial_state = PuzzleState(problem.initial_state, problem)
        open_list = []  # Priority queue for states to be explored.
        heapq.heappush(open_list, initial_state)
        visited = set()  # Set to track visited configurations to prevent re-exploration.
        visited.add(tuple(problem.initial_state))
    
        while open_list:
            current_state = heapq.heappop(open_list)  # Pop the state with the lowest f(n) score.
            if current_state.is_goal():
                return current_state  # Return the solution path if the goal state is reached.
            for child in current_state.generate_children():  # Explore all child states.
                child_config_tuple = tuple(child.configuration) # Makes sure no states are repeated
                if child_config_tuple not in visited:
                    visited.add(child_config_tuple)
                    heapq.heappush(open_list, child)
        return None  # Return None if no solution is found.
        
    def __lt__(self,other):
        self.score < other.score
