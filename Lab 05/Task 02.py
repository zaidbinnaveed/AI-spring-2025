import random
import math

def total_distance(route):
    return sum(math.dist(route[i], route[i+1]) for i in range(len(route)-1))

def hill_climb_shortest_route(points):
    route = points[:]
    random.shuffle(route)
    best_distance = total_distance(route)

    for _ in range(1000):
        i, j = random.sample(range(len(route)), 2)
        new_route = route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_distance = total_distance(new_route)
        if new_distance < best_distance:
            route, best_distance = new_route, new_distance

    return route, best_distance

points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
print(hill_climb_shortest_route(points))
