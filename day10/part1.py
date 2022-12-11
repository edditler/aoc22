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
cycle = 1
instruction = 0
cycles_left = 0
command = ""
arguments = []
signal = [(0, False), (1, False)]

duration = {"noop": 1, "addx": 2}

running = True
while running:
    # print(f"{cycle= }")
    # print(f"{cycles_left=}")

    if cycles_left == 0:
        if command == "addx":
            X += int(arguments[0])

        if instruction == len(program):
            running = False
            break

        command, arguments = program[instruction]
        # print("Start instruction ", command, arguments)
        cycles_left = duration[command]
        instruction += 1

    signal.append((X, cycles_left > 0 and command == "addx"))
    cycle += 1
    cycles_left -= 1

    # print("===")

answer = 0
for i_s in [20, 60, 100, 140, 180, 220]:
    if signal[i_s][1] == True:
        answer += signal[i_s + 1][0] * i_s
    else:
        answer += signal[i_s][0] * i_s

print(f"{answer=}")

# answer=14340
# [Finished in 37ms]
