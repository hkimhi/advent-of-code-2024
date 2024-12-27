import time
import re

start_time = time.time()

with open("input.txt") as infile:
    data = infile.read().split('\n\n')
    a, b, c = list(map(int, re.findall(r"\d+", data[0])))
    prog = list(map(int, data[1].strip().split(': ')[1].split(',')))

def evaluate_program(a, b, c, ip=0, out=[]):
    out_str = ""
    ip = 0  # instruction pointer

    while (ip < len(prog)):
        combo_op = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: a,
            5: b,
            6: c
        }
        instr = prog[ip]
        op = prog[ip + 1]  # literal operand

        match instr:
            case 0:
                # A / (2**(combo op)), truncate to int, write to A
                a = a // (2 ** combo_op[op])
            case 1:
                # B xor literal op, write to B
                b = b ^ op
            case 2:
                # combo op mod 8, store B
                b = combo_op[op] % 8
            case 3:
                # if A != 0, ip <- literal op (do not increase ip by 2)
                if a != 0:
                    ip = op - 2
            case 4:
                # B xor C, store B
                b = b ^ c
            case 5:
                # combo op mod 8, write to out
                out_str += f"{combo_op[op] % 8},"
            case 6:
                # A / (2**(combo op)), truncate to int, write to B
                b = a // (2 ** combo_op[op])
            case 7:
                # A / (2**(combo op)), truncate to int, write to C
                c = a // (2 ** combo_op[op])

        ip += 2

    out = list(map(int, out_str.split(',')[:-1]))
    return out

out = evaluate_program(a, b, c)
print(out, sep=',')

# basically the output only depends on the input a, and specifically only depends on the last 3 bits of a
# so we just need to test specific values of a
def find_a(a, ip):
    if evaluate_program(a, b, c) == prog:
        print(f"Found A: {a}")

    if evaluate_program(a, b, c) == prog[-ip:] or not ip:
        for n in range(8):
            find_a(8 * a + n, ip + 1)

# breakpoint()
find_a(0, 0)  # 202367025818154
print(f"took {time.time() - start_time}s")
