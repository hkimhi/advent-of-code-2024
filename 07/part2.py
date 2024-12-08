import time

equations = []

with open("input.txt") as infile:
    equations = [line.strip() for line in infile.readlines()]

result = 0

def recursive_solver(goal, curr, digits):
    if len(digits) <= 0:
        return curr == goal

    op1 = recursive_solver(goal, curr + digits[0], digits[1:])
    op2 = recursive_solver(goal, curr * digits[0], digits[1:])
    op3 = recursive_solver(goal, int(f"{curr}{digits[0]}"), digits[1:])

    return op1 or op2 or op3

start_time = time.time()
for equation in equations:
    goal, rest = equation.split(': ')
    goal = int(goal)

    nums = [int(_) for _ in rest.split(' ')]
    if (recursive_solver(goal, nums[0], nums[1:])):
        result += goal

print(f"total calibration result: {result}")  # 61561126043536
print(f"took {time.time() - start_time} seconds")
# still slightly better with a "forward" solve using recursion, but also taking a while (3.6s)

# better move would probably to work backwards since we get only increasing operators, so can see
# if the decrease is legal (i.e. is the next number a factor? if not can't multiply, skip that path)
