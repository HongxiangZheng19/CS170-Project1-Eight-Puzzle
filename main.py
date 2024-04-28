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
        self.heuristic = self.euclidean_distance()  # Compute the Euclidean distance heuristic.
        self.score = self.cost + self.heuristic  # Total score f(n) = g(n) + h(n).

    # Find and return the index of the blank tile.
    def find_blank(self):
        return self.configuration.index(0)

    # Calculate the Euclidean distance for each tile from its current position to its goal position.
    def euclidean_distance(self):
        distance = 0
        for i in range(9):
            if self.configuration[i] != 0:
                x, y = divmod(i, 3)
                goal_x, goal_y = divmod(self.problem.goal_state.index(self.configuration[i]), 3)
                distance += math.sqrt((x - goal_x) ** 2 + (y - goal_y) ** 2)
        return distance
    
    # Generate all valid child states by moving the blank tile according to the defined operators.
    def generate_children(self):
        children = []
        x, y = divmod(self.blank_pos, 3)
        for dx, dy in self.problem.operators:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_config = self.configuration[:]
                new_config[self.blank_pos], new_config[new_pos] = new_config[new_pos], new_config[self.blank_pos]
                children.append(PuzzleState(new_config, self.problem, self, new_pos, self.cost + 1))
        return children
    
    # Check if the current configuration matches the goal configuration.
    def is_goal(self):
        return self.configuration == self.problem.goal_state

    # Comparator for priority queue to sort states by their total score.
    def __lt__(self, other):
        return self.score < other.score

    # A* search algorithm implementation.
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
                child_config_tuple = tuple(child.configuration)
                if child_config_tuple not in visited:
                    visited.add(child_config_tuple)
                    heapq.heappush(open_list, child)
        return None  # Return None if no solution is found.

    # Example usage:
    initial_config = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    problem = Problem(initial=initial_config)  # Create a problem instance.
    result = a_star(problem)  # Solve the problem using A* search.
    steps = []
    while result:
        steps.append(result.configuration)
        result = result.parent
    steps.reverse()

    for step in steps:
        print(step)
