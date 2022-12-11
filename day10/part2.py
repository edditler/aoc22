import numpy as np


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

program = []

for line in lines:
    split = line.split(" ")
    if len(split) == 1:
        command = split[0]
        arguments = []
    else:
        command = split[0]
        arguments = split[1:]

    program.append([command, arguments])


X = 1
cycle = 0
instruction = 0
cycles_left = 0
command = ""
arguments = []
display = np.empty((6, 40), dtype=str)
display[:][:] = "."

duration = {"noop": 1, "addx": 2}

running = True
while running:
    print(f"{cycle= }")
    i_pos = cycle % 40
    i_row = cycle // 40

    if cycles_left == 0:
        if command == "addx":
            X += int(arguments[0])

        if instruction == len(program):
            running = False
            break

        command, arguments = program[instruction]
        print("Start instruction ", command, arguments)
        cycles_left = duration[command]
        instruction += 1

    print(f"Drawing in ({i_pos=}, {i_row=})")
    print(f"Sprite around {X}")
    if abs(i_pos - X) <= 1:
        display[i_row, i_pos] = "#"
        print("Was lit!")

    print("=" * 50)
    cycle += 1
    cycles_left -= 1

print("=" * 50)

for line in display:
    print("".join(line))
