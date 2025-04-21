import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
transition_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

state_map = {'Sunny': 0, 'Cloudy': 1, 'Rainy': 2}
current_state = state_map['Sunny']
simulated_states = []

for _ in range(10):
    current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])
    simulated_states.append(current_state)

rainy_days = simulated_states.count(2)
probability_at_least_3_rainy = sum([1 for _ in range(10000) if [np.random.choice([0, 1, 2], p=transition_matrix[current_state]) for _ in range(10)].count(2) >= 3]) / 10000

print(simulated_states)
print(rainy_days)
print(probability_at_least_3_rainy)
