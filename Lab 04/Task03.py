class DeliveryPoint:
    def __init__(self, position, time_window):
        self.position = position
        self.time_window = time_window

def greedy_best_first_delivery(delivery_points, start):
    open_list = []
    heapq.heappush(open_list, (0, start))
    visited = set()
    total_distance = 0
    current_time = 0
    route = [start]

    while open_list:
        _, current_position = heapq.heappop(open_list)
        visited.add(current_position)
        nearest_point = None
        nearest_distance = float('inf')

        for point in delivery_points:
            if point.position not in visited:
                dist = distance(current_position, point.position)
                if dist < nearest_distance and point.time_window[0] <= current_time + dist:
                    nearest_point = point
                    nearest_distance = dist
        
        if nearest_point:
            route.append(nearest_point.position)
            total_distance += nearest_distance
            current_time += nearest_distance
            delivery_points.remove(nearest_point)
            heapq.heappush(open_list, (nearest_distance, nearest_point.position))
    
    return route, total_distance

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
