import copy


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Sensor:
    def __init__(self, sensor, beacon):
        super(Sensor, self).__init__()
        self.sensor = sensor
        self.beacon = beacon
        self.distance = manhattan(self.sensor, self.beacon)

    def __repr__(self) -> str:
        return f"{self.sensor} to {self.beacon}: {self.distance}"


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
max_dim = 4000000

all_sb = []
min_x = 0
max_x = 0
for line in lines:
    s, b = line.split(":")
    sx, sy = s.split(",")
    bx, by = b.split(",")
    sensor_x, sensor_y = int(sx.split("=")[1]), int(sy.split("=")[1])
    beacon_x, beacon_y = int(bx.split("=")[1]), int(by.split("=")[1])
    new_sb = Sensor((sensor_x, sensor_y), (beacon_x, beacon_y))
    all_sb.append(new_sb)

for x in range(0, max_dim + 1):
    if x % 40000 == 0:
        print(f"{x}/{max_dim}")
    for y in range(0, max_dim + 1):
        possible = True
        # print(f"{x=}")
        # Figure out if it's reachable
        for sb in all_sb:
            # print(f"{sb}")
            distance = manhattan(sb.sensor, (x, y))
            if distance <= sb.distance:
                possible = False
                break
        if possible:
            print(x, y, x * 4000000 + y)


# I can't even get 1% through the search space in a few minutes.
# Linear Programming appears to be the solution
# We have a system of constraints:
#  - The solution must be outside of all circles
#  - The solution must be within x \in [0, max_dim+1], y \in [0, max_dim+1]
#  - The solution must be integer
