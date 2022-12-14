import numpy as np

with open("input.txt") as f:
    # Yeah, this is fine
    wall = [
        [
            (int(x), int(y))
            for x, y in [segment.split(",") for segment in line.strip().split("->")]
        ]
        for line in f.readlines()
    ]

# First determine how far we go down and right
max_x = 0
max_y = 0
for segment in wall:
    for corner in segment:
        if corner[0] > max_x:
            max_x = corner[0]

        if corner[1] > max_y:
            max_y = corner[1]

cave = np.zeros((1000, max_y + 1 + 2))

# Mark all walls as 1
for iseg, segment in enumerate(wall):
    for i in range(1, len(segment)):
        print(i - 1, i)
        start = segment[i - 1]
        end = segment[i]
        range_x = (min(start[0], end[0]), max(start[0], end[0]))
        range_y = (min(start[1], end[1]), max(start[1], end[1]))
        print(f"{start=}, {end=}")
        for x in np.arange(range_x[0], range_x[1] + 1):
            for y in np.arange(range_y[0], range_y[1] + 1):
                cave[x, y] = 1
    print()

# Verify the cave
go_on = True
nsand = 0
resting = False

x_s = 500
y_s = 0
cave[x_s, y_s] = 9
cave[:, -1] = 1
print(cave[493:, :].T)
print()

while True:
    if resting:
        # create a new sand corn, if
        # print("Creating a sand corn")
        x_s = 500
        y_s = 0
        resting = False

    # propagate the sand
    if cave[x_s, y_s + 1] == 0:
        y_s += 1
    elif cave[x_s - 1, y_s + 1] == 0:
        y_s += 1
        x_s -= 1
    elif cave[x_s + 1, y_s + 1] == 0:
        y_s += 1
        x_s += 1
    else:
        # print(f"Sand corn {i} came to a rest at ({x_s}, {y_s})")
        nsand += 1
        resting = True
        cave[x_s, y_s] = 2
        if x_s == 500 and y_s == 0:
            break
        # print(f"Step {istep} , {nsand} sands")
        # print(cave[493:, :].T)


print(cave[493:, :].T)
print(nsand)
