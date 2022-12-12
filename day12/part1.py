import numpy as np
import copy

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

height_map_inp = np.array([list(line) for line in lines])

start = np.where(height_map_inp == "S")
end = np.where(height_map_inp == "E")

start_x = start[1][0]
start_y = start[0][0]
end_x = end[1][0]
end_y = end[0][0]

print(start_x, start_y)
print(end_x, end_y)

height_map = np.empty_like(height_map_inp, dtype=int)

for i in range(height_map.shape[0]):
    for j in range(height_map.shape[1]):
        height_map[i, j] = ord(height_map_inp[i, j]) - 97

height_map[start_y, start_x] = ord("a") - 97
height_map[end_y, end_x] = ord("z") - 97
print(height_map)


def reachable_to(x, y, height_map):
    # Returns the reachable nodes from (y, x)
    # Reachable node: if we go down, even, or up by at most 1
    max_y, max_x = height_map.shape
    this_height = height_map[y, x]
    reachable = []
    for dx, dy in [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]:
        if x + dx < 0 or y + dy < 0 or x + dx == max_x or y + dy == max_y:
            continue
        if (
            height_map[y + dy, x + dx] <= this_height
            or height_map[y + dy, x + dx] - this_height == 1
        ):
            reachable.append((dy, dx))
    return reachable


def reachable_from(x, y, height_map):
    # Returns from where (y, x) can be reached
    # Possible: go up, go even, go down by at most 1
    max_y, max_x = height_map.shape
    this_height = height_map[y, x]
    reachable = []
    for dx, dy in [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]:
        if x + dx < 0 or y + dy < 0 or x + dx == max_x or y + dy == max_y:
            continue
        if (
            height_map[y + dy, x + dx] >= this_height
            or height_map[y + dy, x + dx] - this_height == -1
        ):
            reachable.append((dx, dy))
    return reachable


# print("Possible:", possible_moves(0, 0, height_map))
# print("Possible:", possible_moves(1, 1, height_map))
# print("Possible:", possible_moves(7, 4, height_map))


class Path:
    def __init__(self, end, goal):
        self.visited_tiles = [
            end,
        ]
        self.goal = goal
        self.complete = False
        self.failed = False

    def current(self):
        return self.visited_tiles[-1]

    def reached_goal(self):
        if self.goal in self.visited_tiles:
            self.complete = True

        return self.complete

    def move_possible(self, move):
        current = self.current()
        new_tile = [current[0] + move[0], current[1] + move[1]]
        # print("in move_possible")
        # print(f"{current=}")
        # print(f"{new_tile=}")
        # print(f"{self.visited_tiles=}")
        if new_tile in self.visited_tiles:
            return False

        return True

    def add_step(self, move):
        current = self.current()
        new_tile = [current[0] + move[0], current[1] + move[1]]
        self.visited_tiles.append(new_tile)

        if self.reached_goal():
            print(f"Path is at the end! Took {len(self.visited_tiles)} steps")

        return True

    def paint_path(self, height_map):
        solution = np.zeros_like(height_map)
        for i, visited in enumerate(self.visited_tiles[::-1]):
            solution[visited[1], visited[0]] = i + 1

        print(solution)


# Naive implementation
# We start from the end, explore all possible moves and see if we reach the start
paths = [
    Path([end_x, end_y], [start_x, start_y]),
]

niter = 0
go_on = True
while go_on and niter < 100000:
    # print("=" * 80)
    print(f"Iteration {niter+1}")
    # print("Test, if all paths complete")

    paths_to_add = []

    all_complete = True
    for path in paths:
        all_complete = all_complete and path.reached_goal()

    if all_complete:
        # print(f"All {len(paths)} paths reached the goal!")
        go_on = False
        break

    # print(f"No, they are not complete. Try all {len(paths)} paths")
    for ipath, path in enumerate(paths):
        # print(f"{ipath=}")
        if path.reached_goal():
            continue

        current = path.current()
        moves = reachable_from(current[0], current[1], height_map)

        # print(f"Found {len(moves)} moves.")
        possible_moves = list()
        for move in moves:
            if path.move_possible(move):
                possible_moves.append(move)

        # print(f"Found {len(possible_moves)} possible moves.")
        # print(f"{possible_moves=}")

        if len(possible_moves) == 0:
            # print(f"No moves possible for ({ipath})!")
            path.failed = True
            path.complete = True
        elif len(possible_moves) == 1:
            path.add_step(possible_moves[0])
        elif len(possible_moves) > 1:
            # We create additional paths
            current_path = copy.deepcopy(path)
            path.add_step(possible_moves[0])
            for move in possible_moves[1:]:
                new_path = copy.deepcopy(current_path)
                new_path.add_step(move)
                paths_to_add.append(new_path)

    paths += paths_to_add

    niter += 1
    # print(f"After {niter} steps, we have {len(paths)} paths.")
    # for i, path in enumerate(paths):
    # print(f"Path {i}: ", len(path.visited_tiles), path.visited_tiles)
    # print("=" * 80)

print("*" * 80)
steps = []
for path in paths:
    steps.append(len(path.visited_tiles))
    print(path.visited_tiles[-1], len(path.visited_tiles))
    # print(path.visited_tiles[::-1])
    # path.paint_path(height_map)
    # print()

print(sorted(steps)[0] - 1)
