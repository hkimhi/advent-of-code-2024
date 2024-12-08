import itertools

equations = []

with open("input.txt") as infile:
    equations = [line.strip() for line in infile.readlines()]

result = 0
OPERATIONS = ['*', '+', 'concat']

for equation in equations:
    goal, rest = equation.split(': ')
    goal = int(goal)
    nums = [int(_) for _ in rest.split(' ')]
    num_spaces = rest.count(' ')

    for ops in itertools.product(OPERATIONS, repeat=num_spaces):
        curr_val = nums[0]
        for j, op in enumerate(ops):
            if op == '*':
                curr_val *= nums[j + 1]
            elif op == '+':
                curr_val += nums[j + 1]
            elif op == 'concat':
                curr_val = int(str(curr_val) + str(nums[j + 1]))

        if curr_val == goal:
            result += goal
            break

print(f"total calibration result: {result}")  # 61561126043536
# slightly better solution, maybe? should probably run a profiler, still took a while
# better move would probably to work backwards since we get only increasing operators, so can see
# if the decrease is legal (i.e. is the next number a factor? if not can't multiply, skip that path)
