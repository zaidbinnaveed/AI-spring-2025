import time
import copy

row_labels = "LMNOPQRST"
col_labels = "ABCDEFGHI"
num_set = "123456789"

def create_combinations(A, B):
    return [a + b for a in A for b in B]

grid_cells = create_combinations(row_labels, col_labels)
row_units = [create_combinations(r, col_labels) for r in row_labels]
col_units = [create_combinations(row_labels, c) for c in col_labels]
block_units = [create_combinations(rs, cs) for rs in ('LMN', 'OPQ', 'RST') for cs in ('ABC', 'DEF', 'GHI')]

all_units = row_units + col_units + block_units
unit_map = {cell: [unit for unit in all_units if cell in unit] for cell in grid_cells}
neighbors = {cell: set(sum(unit_map[cell], [])) - {cell} for cell in grid_cells}

def decode_grid(grid):
    value_map = {cell: num_set for cell in grid_cells}
    for idx, val in zip(grid_cells, grid):
        if val in num_set and not assign_value(value_map, idx, val):
            return False
    return value_map

def assign_value(value_map, cell, value):
    remaining_values = value_map[cell].replace(value, '')
    if all(remove_value(value_map, cell, val) for val in remaining_values):
        return value_map
    return False

def remove_value(value_map, cell, value):
    if value not in value_map[cell]:
        return value_map
    value_map[cell] = value_map[cell].replace(value, '')
    if len(value_map[cell]) == 0:
        return False
    elif len(value_map[cell]) == 1:
        next_value = value_map[cell]
        if not all(remove_value(value_map, neighbor, next_value) for neighbor in neighbors[cell]):
            return False
    for unit in unit_map[cell]:
        possible_cells = [neighbor for neighbor in unit if value in value_map[neighbor]]
        if len(possible_cells) == 0:
            return False
        elif len(possible_cells) == 1:
            if not assign_value(value_map, possible_cells[0], value):
                return False
    return value_map

def ac3_algorithm(value_map):
    queue = [(cell, neighbor) for cell in grid_cells for neighbor in neighbors[cell]]
    while queue:
        cell, neighbor = queue.pop(0)
        if revise(value_map, cell, neighbor):
            if len(value_map[cell]) == 0:
                return False
            for further_neighbor in neighbors[cell] - {neighbor}:
                queue.append((further_neighbor, cell))
    return value_map

def revise(value_map, cell, neighbor):
    updated = False
    for val in value_map[cell]:
        if len(value_map[neighbor]) == 1 and value_map[neighbor] == val:
            value_map[cell] = value_map[cell].replace(val, '')
            updated = True
    return updated

def is_solved(value_map):
    return all(len(value_map[cell]) == 1 for cell in grid_cells)

def backtrack_search(value_map):
    if value_map is False:
        return False
    if is_solved(value_map):
        return value_map
    min_values, chosen_cell = min((len(value_map[cell]), cell) for cell in grid_cells if len(value_map[cell]) > 1)
    for val in value_map[chosen_cell]:
        new_value_map = copy.deepcopy(value_map)
        if assign_value(new_value_map, chosen_cell, val):
            solution = backtrack_search(new_value_map)
            if solution:
                return solution
    return False

def solve_sudoku(grid):
    parsed_values = decode_grid(grid)
    if parsed_values:
        parsed_values = ac3_algorithm(parsed_values)
        return backtrack_search(parsed_values)
    return None

if __name__ == "__main__":
    input_file_path = "sudoku_input.txt"

    with open(input_file_path, 'r') as file:
        puzzle_list = [line.strip() for line in file if line.strip()]

    for index, puzzle in enumerate(puzzle_list):
        print(f"\nSolving Puzzle #{index + 1}")
        print("Input:")
        for i in range(0, 81, 9):
            print(puzzle[i:i+9])
        
        start_time = time.time()
        solution = solve_sudoku(puzzle)
        end_time = time.time()

        if solution:
            print("\nSolved:")
            for i in range(0, 81, 9):
                print(solution[i:i+9])
        else:
            print("No solution found.")

        print(f"Time taken: {end_time - start_time:.4f} seconds")
