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
    
    # h(n) calculates the number of tiles in the wrong position in the puzzle configuration
    def misplaced_tile_heuristic(self):
        misplaced_tiles = 0
        for i in range(9):
            if self.configuration[i] != 0 and self.configuration[i] != self.problem.goal_state[i]:
                misplaced_tiles += 1
        return misplaced_tiles
    
    def expand_nodes(self):
        frontier = [] # Setup frontier
        
    # Check if the current configuration matches the goal configuration.
    def is_goal(self):
        return self.configuration == self.problem.goal_state
    
    # Generate all valid child states by moving the blank tile according to the defined operators
        # This function is only responsible for generating all possible children state
    def generate_children(self):
        # hold all the child states generated
        children = []

        # attempts to find the position of the blank tile
            # For example, if self.blank_pos is 5, divmod(5, 3) will return (1, 2) -> the blank will be at (row 1, column 2)
        x, y = divmod(self.blank_pos, 3)
        
        # iterates through the possible movements (up, down, left, right)
        for dx, dy in self.problem.operators:
            # calculates the new position (nx, ny) of the blank tile after moving it in the direction (dx, dy)
            nx, ny = x + dx, y + dy

            # make sure that the tile would not go out of bound (3 x 3 grid)
            if 0 <= nx < 3 and 0 <= ny < 3:
                # translates the 2D grid coordinates back into a 1D index (list of length 9)
                new_pos = nx * 3 + ny
                # creates a copy of the current configuration 
                    # avoids modifying the original configuration
                new_config = self.configuration[:]
                # swaps the blank tile with the tile at the new position
                new_config[self.blank_pos], new_config[new_pos] = new_config[new_pos], new_config[self.blank_pos]
                # creates a new PuzzleState object for the child state
                    # It passes the parameter of:
                        # new configuration
                        # problem instance
                        # current state as the parent
                        # new position of the blank tile
                        # updated cost (incremented by 1 since each move has a cost of 1)
                children.append(PuzzleState(new_config, self.problem, self, new_pos, self.cost + 1))
        # returns the list of all valid child states generated
        return children
    

def misplace_search(problem):
    # to be done 
    return None


# User Interface

print("Welcome to XXX (change this to your student ID) 8 puzzle solver.")
x = int(input('Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n'))
if x == 1: 
    print('Default puzzle\n')
    initial_config = [1, 2, 3, 4, 8, 0, 7, 6, 5] 

elif x == 2:
    print('Enter your puzzle, use a zero to represent the blank')
    a1, a2, a3 = get_valid_input('Enter the first row, use space or tabs between numbers ', 3)
    b1, b2, b3 = get_valid_input('Enter the second row, use space or tabs between numbers ', 3)
    c1, c2, c3 = get_valid_input('Enter the third row, use space or tabs between numbers ', 3)
    print('\n')
    initial_config = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
else:
    print("Invalid puzzle choice.")
    exit()

print('Enter your choice of algorithm')
print('Uniform Cost Search')
print('A* with the Misplaced Tile heuristic.')
print('A* with the Euclidean distance heuristic.')

algorithm_call = int(input('Choose your option (1, 2, or 3): '))

problem = Problem(initial=initial_config)
result = None
if algorithm_call == 1:
    print('UCS not implemented yet')
elif algorithm_call == 2:
    result, max_heap_size = misplace_search(problem)
elif algorithm_call == 3:
    print('A* Euclidean not implemented yet')
else:
    print("Invalid algorithm choice.")

if result:
    steps = []
    while result:
        steps.append(result.configuration)
        result = result.parent
    steps.reverse()
    print("Solution path:")
    for step in steps:
        print(step)
    print(f"Maximum heap size during the search was: {max_heap_size}")
else:
    print("No solution found.")
    print(f"Maximum heap size during the search was: {max_heap_size}")