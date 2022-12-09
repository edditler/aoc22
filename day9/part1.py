import numpy as np
import sys

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
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


def printMap(head, tail, history=False):
    max_x = 0
    max_y = 0
    for x, y in tail.touched_coordinates:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    field = np.zeros((max(max_x, max_y) + 5, max(max_x, max_y) + 5))
    # field = np.zeros((6, 6))

    if history:
        for x, y in tail.touched_coordinates:
            # print(f"Touched", x, y)
            field[x, y] = 1

    field[tail.x, tail.y] = 1
    if not history:
        field[head.x, head.y] += 2
    print(field.T[::-1])
    print("=" * 50)
    return field


head = Coordinates(250, 250)
tail = Coordinates(250, 250)

# I was overthinking this. You can't actually get the move from the
#  sine and cosine of the angle directly.
# But there aren't too many possible moves. part2.py has the correct map.
moves = {
    0.0: (1, 0),
    1.1: (1, 1),
    1.6: (0, 1),
    -1.6: (0, -1),
    3.1: (-1, 0),
    2.7: (-1, 1),
    -0.5: (1, -1),
    -2.7: (-1, -1),
    -2: (-1, -1),
    0.5: (1, 1),
    2.0: (-1, 1),
    -1.1: (1, -1),
}

for line in lines:
    # print(line)
    direction, n = line.split()
    n = int(n)
    # print(f"Start of turn: {head=} {tail=}")
    for i in range(n):
        head.moveD(direction)

        do_touch = are_touching(head, tail)
        x = head.x - tail.x
        y = head.y - tail.y
        atan = np.round(np.arctan2(y, x), 1)

        if do_touch:
            pass
        else:
            if atan in moves.keys():
                tail.moveC(moves[atan])
            else:
                # print(head, tail)
                # print(f"{are_diagonal(head, tail)}")
                # print(f"{atan=}")
                printMap(head, tail)
                sys.exit("Not touching at the end!")

        # print(f"{head=} {tail=}")
        # printMap(head, tail)

# Print the map
final = printMap(head, tail, True)
print(np.sum(final))

# 5513.0
# [Finished in 312ms]
