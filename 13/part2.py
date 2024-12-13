import time
from sympy import solve, symbols, Integer

start_time = time.time()

machines = []

with open("input.txt") as infile:
    for m in infile.read().split('\n\n'):
        lines = m.split('\n')
        dx_a, dy_a = map(int, lines[0].split(': ')[1].replace('X+', '').replace('Y+', '').split(', '))
        dx_b, dy_b = map(int, lines[1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', '))
        x_g, y_g = map(int, lines[2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', '))
        x_g += 10000000000000
        y_g += 10000000000000
        machines.append((dx_a, dy_a, dx_b, dy_b, x_g, y_g))

def solve_machine(dx_a, dy_a, dx_b, dy_b, x_g, y_g):
    n_a, n_b = symbols('na nb')
    result = solve([n_a * dx_a + n_b * dx_b - x_g, n_a * dy_a + n_b * dy_b - y_g], dict=True)
    num_a = result[0][n_a]
    num_b = result[0][n_b]

    if isinstance(num_a, Integer) and isinstance(num_b, Integer):
        return num_a, num_b
    else:
        return None, None

def calculate_tokens():
    total_prizes = 0
    total_tokens = 0

    for machine in machines:
        dx_a, dy_a, dx_b, dy_b, x_g, y_g = machine
        n_a, n_b = solve_machine(dx_a, dy_a, dx_b, dy_b, x_g, y_g)
        if n_a is not None and n_b is not None:
            total_prizes += 1
            total_tokens += 3 * n_a + n_b

    return total_prizes, total_tokens

print(f"token cost: {calculate_tokens()[1]}")  # 85644161121698
print(f"took {time.time() - start_time}s")
