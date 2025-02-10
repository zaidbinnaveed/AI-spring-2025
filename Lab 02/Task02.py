import sys

class Graph:
    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances
        self.num_cities = len(cities)

    def get_distance(self, city1, city2):
        return self.distances[city1][city2]

    def get_neighbors(self, city):
        return [i for i in range(self.num_cities) if i != city]


def iterative_deepening_dfs(graph, start_city, goal_city):
    def dfs(city, visited, depth):
        if depth == 0:
            return [city] if city == goal_city else None
        visited.add(city)
        for neighbor in graph.get_neighbors(city):
            if neighbor not in visited:
                path = dfs(neighbor, visited, depth - 1)
                if path:
                    return [city] + path
        return None

    depth = 0
    while True:
        visited = set()
        path = dfs(start_city, visited, depth)
        if path:
            return path
        depth += 1


def bidirectional_search(graph, start_city, goal_city):
    def bfs(frontier, explored, graph, start_city):
        queue = [start_city]
        paths = {start_city: [start_city]}
        while queue:
            city = queue.pop(0)
            for neighbor in graph.get_neighbors(city):
                if neighbor not in explored:
                    explored.add(neighbor)
                    queue.append(neighbor)
                    paths[neighbor] = paths[city] + [neighbor]
                    if neighbor in frontier:
                        return paths[neighbor]
        return None

    frontier_start = {start_city}
    frontier_goal = {goal_city}
    explored_start = {start_city}
    explored_goal = {goal_city}

    path_start = bfs(frontier_start, explored_start, graph, start_city)
    if path_start:
        return path_start

    path_goal = bfs(frontier_goal, explored_goal, graph, goal_city)
    if path_goal:
        return path_goal

    return None


def total_distance(path, graph):
    return sum(graph.get_distance(path[i], path[i + 1]) for i in range(len(path) - 1))


def traveling_salesman(graph):
    shortest_path = None
    shortest_distance = sys.maxsize
    for start_city in range(graph.num_cities):
        for goal_city in range(graph.num_cities):
            if start_city != goal_city:
                path = iterative_deepening_dfs(graph, start_city, goal_city)
                if path:
                    distance = total_distance(path, graph)
                    if distance < shortest_distance:
                        shortest_distance = distance
                        shortest_path = path
    return shortest_path, shortest_distance


cities = ['A', 'B', 'C', 'D']
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

graph = Graph(cities, distances)
shortest_path, shortest_distance = traveling_salesman(graph)
print(f"Shortest Path: {shortest_path} with Total Distance: {shortest_distance}")
