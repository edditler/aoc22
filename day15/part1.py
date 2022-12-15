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
row = 2000000

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

    if abs(sensor_y - row) <= new_sb.distance:
        all_sb.append(new_sb)
        min_x = min([min_x, sensor_x - new_sb.distance])
        max_x = max([max_x, sensor_x + new_sb.distance])
        print(new_sb)

print(min_x, max_x)
count = 0
relevant_sb = copy.copy(all_sb)
for x in range(min_x, max_x + 1):
    # print(f"{x=}")
    # Figure out if it's reachable
    for i_sb, sb in enumerate(relevant_sb):
        # print(f"{sb}")
        distance = manhattan(sb.sensor, (x, row))
        if distance <= sb.distance:
            # print(f"Distance to our point: {distance}")
            count += 1
            break
        if sb.sensor[0] < x - sb.distance:
            print(f"Deleted {i_sb}, because {sb.sensor[0]=} {x=}")
            del relevant_sb[i_sb]


print("=" * 20)
# We also need to subtract the beacons on this line:
considered_beacons = []
for sb in relevant_sb:
    if sb.beacon[1] == row:
        if sb.beacon not in considered_beacons:
            considered_beacons.append(sb.beacon)
            count -= 1
            print(sb)
        continue

print(f"{count=}")


# count=5461729
# [Finished in 19.5s]
# Maybe the loop over grid points and sensors should be swapped, but then we would
# need to keep track of where we are.
