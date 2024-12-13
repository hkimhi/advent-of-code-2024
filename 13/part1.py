import time
import numpy as np

start_time = time.time()

machines = []

with open("input.txt") as infile:
    for m in infile.read().split('\n\n'):
        lines = m.split('\n')
        dx_a, dy_a = map(int, lines[0].split(': ')[1].replace('X+', '').replace('Y+', '').split(', '))
        dx_b, dy_b = map(int, lines[1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', '))
        x_g, y_g = map(int, lines[2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', '))
        machines.append((dx_a, dy_a, dx_b, dy_b, x_g, y_g))

def solve_machine(dx_a, dy_a, dx_b, dy_b, x_g, y_g):
    # will be solving A * N = B, where
    # A = [dx_a, dx_b], [dy_a, dy_b]
    # N = [n_a, n_b]
    # B = [x_g, y_g]
    A = np.array([[dx_a, dx_b], [dy_a, dy_b]])
    B = np.array([x_g, y_g])

    try:
        solution = np.linalg.solve(A, B)
        n_a, n_b = solution

        if n_a >= 0 and n_b >= 0 and np.isclose(n_a, round(n_a), atol=1e-9) and np.isclose(n_b, round(n_b), atol=1e-9):
            return round(n_a), round(n_b)
        else:
            return None, None
    except np.linalg.LinAlgError:
        # not invertible -> no solution
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

print(f"token cost: {calculate_tokens()[1]}")  # 34787
print(f"took {time.time() - start_time}s")
