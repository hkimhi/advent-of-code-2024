equations = []

with open("input.txt") as infile:
    equations = [line.strip() for line in infile.readlines()]

result = 0

for equation in equations:
    goal, rest = equation.split(': ')
    goal = int(goal)
    nums = [int(_) for _ in rest.split(' ')]
    num_spaces = rest.count(' ')
    num_permutations = 2**num_spaces

    for i in range(num_permutations):
        curr_val = nums[0]
        for j in range(num_spaces):
            # j-th bit value is (i >> j) & 1
            new_char = '*' if (i >> j) & 1 == 1 else '+'
            if new_char == '*':
                curr_val *= nums[j+1]
            elif new_char == '+':
                curr_val += nums[j+1]

        if curr_val == goal:
            result += goal
            break

print(f"total calibration result: {result}")  # 6392012777720
