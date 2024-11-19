class Node:
    def __init__(self, state, parent, action):
        self.state = state        # Tuple (x, y)
        self.parent = parent      # Parent Node
        self.action = action      # Action taken to reach this state 
        

class Stack_Frontier:
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)
    
    def state_contained(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            return self.frontier.pop()  # LIFO for DFS

def dfs(graph, start_state, goal_state):
    frontier = Stack_Frontier()  # Instantiate the frontier
    start_node = Node(state=start_state, parent=None, action=None)
    frontier.add(start_node)

    visited = set()

    while not frontier.empty():
        current_node = frontier.remove()
        current_state = current_node.state

        if current_state == goal_state:
            # Reconstruct the path
            actions = []
            states = []
            while current_node.parent is not None:
                actions.append(current_node.action)
                states.append(current_node.state)
                current_node = current_node.parent
            states.append(start_state)
            actions.reverse()
            states.reverse()
            return actions, states  # Return the solution path

        if current_state in visited:
            continue  # Skip already visited states
        visited.add(current_state)

        for action, neighbor in graph[current_state]:
            if neighbor not in visited and not frontier.state_contained(neighbor):
                child = Node(state=neighbor, parent=current_node, action=action)
                frontier.add(child)
    return None   # If no solution exists

def get_waterjug_graph(capacities):
    c1, c2 = capacities
    graph = {}
    for x in range(c1 + 1):
        for y in range(c2 + 1):
            state = (x, y)
            actions = []

            # Operation 1: Empty Jug1
            actions.append(("empty jug 1", (0, y)))

            # Operation 2: Empty Jug2
            actions.append(("empty jug 2", (x, 0)))

            # Operation 3: Fill Jug1
            actions.append(("fill jug 1", (c1, y)))

            # Operation 4: Fill Jug2
            actions.append(("fill jug 2", (x, c2)))

            # Operation 5: Pour Jug1 to Jug2
            transferable = min(x, c2 - y)
            new_state = (x - transferable, y + transferable)
            actions.append(("pour jug 1 to jug 2", new_state))  # Corrected

            # Operation 6: Pour Jug2 to Jug1
            transferable = min(y, c1 - x)
            new_state = (x + transferable, y - transferable)
            actions.append(("pour jug 2 to jug 1", new_state))  # Corrected

            graph[state] = actions
    return graph

def waterjug(capacities, start_state, goal_state):
    graph = get_waterjug_graph(capacities)
    return dfs(graph, start_state, goal_state)


# Example Usage:
if __name__ == "__main__":
    # Define jug capacities
    c1 = 5  # Capacity of Jug1
    c2 = 3  # Capacity of Jug2
    capacities = (c1, c2)
    
    # Define start and goal states
    start_state = (0, 0)      # Both jugs are empty
    goal_state = (2, 0)       # Goal: 2 liters in Jug1
    
    result = waterjug(capacities, start_state, goal_state)
    
    if result:
        actions, path = result
        print("Path to goal:")
        for i, state in enumerate(path):
            print(f"Step {i}: {state}")
            if i < len(actions):
                print(f"  Action: {actions[i]}")
    
    else:
        print("No solution found.")
    print("Karan Singh Ghugtyal , 2202301530023")