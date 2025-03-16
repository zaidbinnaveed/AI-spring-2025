import random
import math

def distance(a, b):
    return math.dist(a, b)

def total_route_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

def genetic_tsp(cities, population_size=100, generations=500):
    population = [random.sample(cities, len(cities)) for _ in range(population_size)]
    
    for _ in range(generations):
        population.sort(key=total_route_distance)
        next_gen = population[:10]

        while len(next_gen) < population_size:
            p1, p2 = random.choices(population[:50], k=2)
            child = crossover(p1, p2)
            if random.random() < 0.2:
                mutate(child)
            next_gen.append(child)

        population = next_gen

    best_route = min(population, key=total_route_distance)
    return best_route, total_route_distance(best_route)

cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
print(genetic_tsp(cities))
