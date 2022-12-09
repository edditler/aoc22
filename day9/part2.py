import numpy as np
import sys


class Coordinates:
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i
        self.touched_coordinates = [(x, y)]

    def moveD(self, direction):
        if direction == "R":
            self.moveRight()
        elif direction == "L":
            self.moveLeft()
        elif direction == "U":
            self.moveUp()
        elif direction == "D":
            self.moveDown()

        self.touched_coordinates.append((self.x, self.y))

    def moveC(self, c):
        self.x += c[0]
        self.y += c[1]
        self.touched_coordinates.append((self.x, self.y))

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def are_touching(head, tail):
    return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1


def are_diagonal(head, tail):
    return abs(head.x - tail.x) > 0 and abs(head.y - tail.y) > 0


def printMap(beads):
    max_x = 5
    max_y = 5
    for bead in beads:
        for x, y in bead.touched_coordinates:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    field = np.empty((max(max_x, max_y) + 1, max(max_x, max_y) + 1), dtype=str)
    field[:, :] = "."

    for bead in reversed(beads):
        field[bead.x, bead.y] = str(bead.i)

    field[beads[0].x, beads[0].y] = "H"

    tf = field.T[::-1]
    for line in tf:
        print("".join(line))
    print("=" * 50)
    return field


def printTail(beads):
    max_x = 5
    max_y = 5
    for bead in beads:
        for x, y in bead.touched_coordinates:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    field = np.empty((max(max_x, max_y) + 1, max(max_x, max_y) + 1), dtype=str)
    field[:, :] = "."

    tail = beads[-1]
    for x, y in tail.touched_coordinates:
        field[x, y] = "1"

    tf = field.T[::-1]
    for line in tf:
        print("".join(line))
    print("=" * 50)
    return field


moves = {
    (2, 0): (1, 0),
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (-2, 0): (-1, 0),
    #
    (1, 2): (1, 1),
    (-2, 1): (-1, 1),
    (2, -1): (1, -1),
    (-2, -1): (-1, -1),
    (-1, -2): (-1, -1),
    (2, 1): (1, 1),
    (-1, 2): (-1, 1),
    (1, -2): (1, -1),
    #
    (2, 2): (1, 1),
    (-2, 2): (-1, 1),
    (2, -2): (1, -1),
    (-2, -2): (-1, -1),
}

# -1 is the tail
# 0 is the head
beads = [Coordinates(1000, 1000, i) for i in range(10)]
# beads = [Coordinates(0, 0, i) for i in range(10)]
nbeads = len(beads)
printMap(beads)


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

istep = 0
for line in lines:
    print(line)
    direction, n = line.split()
    n = int(n)
    # print(f"Start of turn: {head=} {beads[1]=}")
    for i in range(n):
        # We first move the head.
        beads[0].moveD(direction)
        print(f"moved {0}")

        # All beads must follow their lead
        for i in range(1, len(beads)):
            istep += 1
            print(f"{istep=}")
            # print(f"lead: {i-1}, follow: {i}")
            lead = beads[i - 1]
            follow = beads[i]

            do_touch = are_touching(lead, follow)
            x = lead.x - follow.x
            y = lead.y - follow.y

            if do_touch:
                pass
            else:
                if (x, y) in moves.keys():
                    follow.moveC(moves[(x, y)])
                    print(f"moved {i}")
                else:
                    printMap(beads)
                    print(f"Touching: {lead=} {follow=}")
                    print(f"{(x, y)=} {np.round(np.arctan2(y, x), 1)=}")
                    sys.exit("Not touching at the end!")

            # printMap(beads)
    # [print(f"i = {bead}") for i, bead in enumerate(beads)]

# Print the map
final = printTail(beads)
print(len(np.where(final == "1")[0]))

# 2427
# [Finished in 689ms]
