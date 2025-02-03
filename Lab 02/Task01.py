class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        return "Goal reached" if percept == self.goal else "Searching"

    def act(self, percept, environment):
        return f"Goal {self.goal} found!" if self.formulate_goal(percept) == "Goal reached" else environment.search(percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def search(self, start, goal):
        return "Implement specific search method"

class DFSAgent(GoalBasedAgent):
    pass

class DFSEnvironment(Environment):
    def search(self, start, goal):
        visited, stack = [], [start]
        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")
            if node == goal:
                return f"Goal {goal} found!"
            for neighbor in reversed(self.graph.get(node, [])):
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        return "Goal not found"

class DLSAgent(GoalBasedAgent):
    def __init__(self, goal, depth_limit):
        super().__init__(goal)
        self.depth_limit = depth_limit

class DLSEnvironment(Environment):
    def search(self, start, goal, depth_limit):
        def dfs(node, depth):
            if depth > depth_limit:
                return None
            visited.append(node)
            if node == goal:
                return f"Goal {goal} found!"
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    result = dfs(neighbor, depth + 1)
                    if result:
                        return result
            visited.pop()
            return None

        visited = []
        return dfs(start, 0) or "Goal not found"

class UCSAgent(GoalBasedAgent):
    pass

class UCSEnvironment(Environment):
    def search(self, start, goal):
        frontier, visited, cost_so_far, came_from = [(start, 0)], set(), {start: 0}, {start: None}
        while frontier:
            frontier.sort(key=lambda x: x[1])
            current_node, current_cost = frontier.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                return f"Goal found with UCS. Path: {list(reversed(path))}, Total Cost: {current_cost}"
            for neighbor, cost in self.graph[current_node].items():
                new_cost = current_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    frontier.append((neighbor, new_cost))
        return "Goal not found"

def tsp(graph, start):
    from itertools import permutations
    min_cost, best_path = float('inf'), None
    cities = list(graph.keys())
    for path in permutations(cities):
        if path[0] == start:
            cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)) + graph[path[-1]][start]
            if cost < min_cost:
                min_cost, best_path = cost, path
    return best_path + (start,), min_cost

class IterativeDeepening:
    def __init__(self, tree, goal, max_depth):
        self.tree, self.goal, self.max_depth = tree, goal, max_depth

    def dls(self, node, depth, path):
        if depth == 0:
            return False
        if node == self.goal:
            path.append(node)
            return True
        if node not in self.tree:
            return False
        for child in self.tree[node]:
            if self.dls(child, depth - 1, path):
                path.append(node)
                return True
        return False

    def search(self, start):
        for depth in range(self.max_depth + 1):
            path = []
            if self.dls(start, depth, path):
                return list(reversed(path))
        return "Goal not found within depth limit."

def bidirectional_search(graph, start, goal):
    from collections import deque
    fwd_queue, bwd_queue = deque([start]), deque([goal])
    fwd_visited, bwd_visited = {start}, {goal}
    while fwd_queue and bwd_queue:
        fwd_node, bwd_node = fwd_queue.popleft(), bwd_queue.popleft()
        if fwd_node in bwd_visited or bwd_node in fwd_visited:
            return "Path found"
        for neighbor in graph[fwd_node]:
            if neighbor not in fwd_visited:
                fwd_visited.add(neighbor)
                fwd_queue.append(neighbor)
        for neighbor in graph[bwd_node]:
            if neighbor not in bwd_visited:
                bwd_visited.add(neighbor)
                bwd_queue.append(neighbor)
    return "No path found"

tree = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H'], 'E': [], 'F': ['I'], 'G': [], 'H': [], 'I': []}
graph = {'A': {'B': 2, 'C': 1}, 'B': {'D': 4, 'E': 3}, 'C': {'F': 1, 'G': 5}, 'D': {'H': 2}, 'E': {}, 'F': {'I': 6}, 'G': {}, 'H': {}, 'I': {}}
tsp_graph = {'A': {'B': 10, 'C': 15, 'D': 20}, 'B': {'A': 10, 'C': 35, 'D': 25}, 'C': {'A': 15, 'B': 35, 'D': 30}, 'D': {'A': 20, 'B': 25, 'C': 30}}

dfs_env, dfs_agent = DFSEnvironment(tree), DFSAgent('I')
print(dfs_agent.act(dfs_env.get_percept('A'), dfs_env))

dls_env, dls_agent = DLSEnvironment(tree), DLSAgent('I', 3)
print(dls_env.search('A', 'I', dls_agent.depth_limit))

ucs_env, ucs_agent = UCSEnvironment(graph), UCSAgent('I')
print(ucs_env.search('A', 'I'))

print(tsp(tsp_graph, 'A'))

ids = IterativeDeepening(tree, 'I', 5)
print(ids.search('A'))

graph_unweighted = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H'], 'E': [], 'F': ['I'], 'G': [], 'H': [], 'I': []}
print(bidirectional_search(graph_unweighted, 'A', 'I'))
