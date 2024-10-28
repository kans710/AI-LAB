class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
def dfs(graph, start_state, goal_state):
    # Initialize the frontier with the starting node
    start_node = Node(state=start_state, parent=None, action=None)
    frontier = StackFrontier()
    frontier.add(start_node)

    # Set to keep track of visited nodes
    visited = set()

    # Loop until the frontier is empty
    while not frontier.empty():
        # Remove a node from the frontier (LIFO - Stack behavior)
        current_node = frontier.remove()
        current_state = current_node.state

        # Check if the current node is the goal
        if current_state == goal_state:
            # If goal is found, reconstruct the path from start to goal
            actions = []
            cells = []
            while current_node.parent is not None:
                actions.append(current_node.action)
                cells.append(current_node.state)
                current_node = current_node.parent
            cells.append(start_state)  # Add start state
            cells.reverse()  # Reverse the path
            return actions, cells  # Return actions and path

        # Mark the node as visited
        visited.add(current_state)

        # Expand the current node's neighbors
        for action, neighbor in graph[current_state]:
            if neighbor not in visited and not frontier.state_contained(neighbor):
                child = Node(state=neighbor, parent=current_node, action=action)
                frontier.add(child)

    return None

graph = {
    'A': [('B', 'B'), ('C', 'C')],
    'B': [('D', 'D'), ('E', 'E')],
    'C': [('F', 'F')],
    'D': [],
    'E': [('F', 'F')],
    'F': []
}
start = 'A'
goal = 'F'
result = dfs(graph, start, goal)

if result:
    actions, path = result
    print("Path to goal:", path)
    print("Actions taken:", actions)
else:
    print("No solution found.")