with open("input.txt") as f:
    lines = f.readlines()

# lines = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2""".splitlines()

# Get the initial layout
## Number of stacks
nstacks = 0
n_initial = 0
for i, line in enumerate(lines):
    if line == "\n":
        nstacks = len(lines[i - 1].split())
        n_initial = i - 1
        break

## These are the initial stackings
print(f"There are {nstacks} stacks")
stack = [None] * nstacks

for line in lines[:n_initial][::-1]:
    this_line = []
    for i_stack in range(nstacks):
        this_line.append(line[i_stack * 4 : i_stack * 4 + 3])

    for i, item in enumerate(this_line):
        if "[" in item:
            if isinstance(stack[i], list):
                stack[i].append(item)
            else:
                stack[i] = [
                    item,
                ]
print("Initial stacks:")
for i_stack in range(nstacks):
    print(f"{i_stack}: {stack[i_stack]}")

## Now do the moves
for operation in lines[n_initial + 2 :]:
    nmoves, _, source, _, destination = operation.split()[1:]
    nmoves, source, destination = int(nmoves), int(source) - 1, int(destination) - 1
    a = stack[source][-nmoves:]
    # print(f"{a=}")
    del stack[source][-nmoves:]
    for item in a:
        stack[destination].append(item)

    print("Now stacks:")
    for i_stack in range(nstacks):
        print(f"{i_stack}: {stack[i_stack]}")
    print("=" * 20)

## Get the top one each:
for i_stack in range(nstacks):
    a = stack[i_stack][-1].replace("[", "").replace("]", "")
    print(a, end="")
print()
