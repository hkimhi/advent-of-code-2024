from enum import Enum

equations = []

with open("input.txt") as infile:
    equations = [line.strip() for line in infile.readlines()]

result = 0

class Operations(Enum):
    MULTIPLY = 0
    ADD = 1
    CONCATENATE = 2

for equation in equations:
    goal, rest = equation.split(': ')
    goal = int(goal)
    nums = [int(_) for _ in rest.split(' ')]
    num_spaces = rest.count(' ')
    num_permutations = 3**num_spaces

    for i in range(num_permutations):
        my_str = ""
        curr_val = nums[0]
        for j in range(num_spaces):
            operation = (i // (3 ** j)) % 3
            op = Operations(operation)
            
            if op == Operations.MULTIPLY:
                curr_val *= nums[j+1]
            elif op == Operations.ADD:
                curr_val += nums[j+1]
            elif op == Operations.CONCATENATE:
                curr_val = int(str(curr_val) + str(nums[j+1]))

        if curr_val == goal:
            result += goal
            break

print(f"total calibration result: {result}")  # 61561126043536
# LMAO naive solution takes a while (obviously, 3**n is kinda large compared to 2**n)
