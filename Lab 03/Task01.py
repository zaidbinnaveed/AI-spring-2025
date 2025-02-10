import heapq

class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        return self.f < other.f

def best_first_search(maze, start, goals):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, Node(start, 0, heuristic(start, goals[0])))
    visited_goals = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position in visited_goals:
            continue

        visited_goals.add(current_node.position)
        if len(visited_goals) == len(goals):
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.position)
        neighbors = get_neighbors(current_node.position)
        for neighbor in neighbors:
            if neighbor not in closed_list:
                g = current_node.g + 1
                h = heuristic(neighbor, goals[0])
                heapq.heappush(open_list, Node(neighbor, g, h, current_node))

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position):
    return [(position[0]+1, position[1]), (position[0]-1, position[1]), (position[0], position[1]+1), (position[0], position[1]-1)]
