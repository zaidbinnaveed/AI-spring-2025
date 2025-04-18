import random

task_durations = [5, 8, 4, 7, 6, 3, 9]
limits = [24, 30, 28]

pricing = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

POOL_SIZE = 6
MIX_CHANCE = 0.8
TWEAK_PROB = 0.2
CYCLES = 20

def create_individual():
    return [random.randint(0, 2) for _ in range(len(task_durations))]

def assess(ind):
    usage = [0] * 3
    cost = 0
    for idx, loc in enumerate(ind):
        hours = task_durations[idx]
        usage[loc] += hours
        cost += hours * pricing[idx][loc]
    overflow = sum((usage[i] - limits[i]) * 100 for i in range(3) if usage[i] > limits[i])
    return cost + overflow

def select(pop, scores):
    s = sum(1 / val for val in scores)
    target = random.uniform(0, s)
    pointer = 0
    for i, sc in enumerate(scores):
        pointer += 1 / sc
        if pointer >= target:
            return pop[i]

def mix(a, b):
    idx = random.randint(1, len(a) - 2)
    return a[:idx] + b[idx:], b[:idx] + a[idx:]

def tweak(ind):
    x, y = random.sample(range(len(ind)), 2)
    ind[x], ind[y] = ind[y], ind[x]

def run():
    pool = [create_individual() for _ in range(POOL_SIZE)]

    for step in range(CYCLES):
        evaluations = [assess(ch) for ch in pool]
        print(f"Cycle {step+1}: Top score = {min(evaluations)}")

        next_gen = []
        while len(next_gen) < POOL_SIZE:
            one = select(pool, evaluations)
            two = select(pool, evaluations)
            if random.random() < MIX_CHANCE:
                a, b = mix(one, two)
            else:
                a, b = one[:], two[:]
            next_gen.extend([a, b])

        for k in range(len(next_gen)):
            if random.random() < TWEAK_PROB:
                tweak(next_gen[k])

        pool = next_gen[:POOL_SIZE]

    final_scores = [assess(ch) for ch in pool]
    winner = pool[final_scores.index(min(final_scores))]

    print("\nOptimized Assignment:")
    for t, l in enumerate(winner):
        print(f"Job {t+1} -> Unit {l+1}")
    print("Optimal Cost:", min(final_scores))

run()
