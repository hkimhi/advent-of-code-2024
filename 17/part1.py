import time
import re

start_time = time.time()

with open("input.txt") as infile:
    data = infile.read().split('\n\n')
    regs = list(map(int, re.findall(r"\d+", data[0])))
    prog = list(map(int, data[1].strip().split(': ')[1].split(',')))


def get_combo_operand(operand):
    if operand <= 3:
        return operand
    else:
        # 4 = A = regs[0], 5 = B = regs[1], 6 = C = regs[2]
        return regs[operand - 4]

out = ""
ip = 0  # instruction pointer
while (ip < len(prog)):
    instr = prog[ip]
    op = prog[ip + 1]  # literal operand

    match instr:
        case 0:
            # A / (2**(combo op)), truncate to int, write to A
            op = get_combo_operand(op)
            regs[0] = regs[0] // (2 ** op)
            ip += 2
        case 1:
            # B xor literal op, write to B
            regs[1] = regs[1] ^ op
            ip += 2
        case 2:
            # combo op mod 8, store B
            op = get_combo_operand(op)
            regs[1] = op % 8
            ip += 2
        case 3:
            # if A != 0, ip <- literal op (do not increase ip by 2)
            if regs[0] != 0:
                ip = op
            else:
                ip += 2
        case 4:
            # B xor C, store B
            regs[1] = regs[1] ^ regs[2]
            ip += 2
        case 5:
            # combo op mod 8, write to out
            op = get_combo_operand(op)
            out += f"{op % 8},"
            ip += 2
        case 6:
            # A / (2**(combo op)), truncate to int, write to B
            op = get_combo_operand(op)
            regs[1] = regs[0] // (2 ** op)
            ip += 2
        case 7:
            # A / (2**(combo op)), truncate to int, write to C
            op = get_combo_operand(op)
            regs[2] = regs[0] // (2 ** op)
            ip += 2

out = out[:-1]  # drop last comma
print(f"output: {out}")  # 1,3,7,4,6,4,2,3,5
print(f"took {time.time() - start_time}s")
