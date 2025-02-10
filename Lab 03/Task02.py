import random
import time

class DynamicNode:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        return self.f < other.f

def a_star_dynamic(maze, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, DynamicNode(start, 0, heuristic(start, goal)))
    
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.position)
        neighbors = get_neighbors(current_node.position)
        for neighbor in neighbors:
            if neighbor not in closed_list:
                edge_cost = random.randint(1, 10)
                g = current_node.g + edge_cost
                h = heuristic(neighbor, goal)
                heapq.heappush(open_list, DynamicNode(neighbor, g, h, current_node))
        
        # Simulate dynamic change in edge costs
        time.sleep(1)
