import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def turn_input_into_grid(lines):
    output = []
    for line in lines:
        output.append(list(line))
    return output

grid = np.array(turn_input_into_grid(lines), dtype=int).T
nx, ny = grid.shape

print(grid)
print(grid.shape)
print("="*70)

visible = np.zeros_like(grid)

# The edges are visible
visible[0, :] = True
visible[:, 0] = True
visible[:, ny-1] = True
visible[nx-1, :] = True

# Check the cross of each
for x in range(1, nx-1):
    for y in range(1, ny-1):
        this_tree = grid[x, y]
        # print(f"{x=} {y=} = {this_tree}")
        # print(grid[0:x, y])
        # print(grid[x+1:, y])

        # Visible from left or right
        if this_tree > max(grid[0:x, y]) or this_tree > max(grid[x+1:, y]):
            visible[x, y] = True
            continue

        # Visible from top or bottom
        if this_tree > max(grid[x, 0:y]) or this_tree > max(grid[x, y+1:]):
            visible[x, y] = True
            continue

print(visible)
print(np.sum(visible))
print("="*70)

# Took 300ms, seems okay

# Part 2
view_score = np.zeros_like(visible)
for x in range(1, nx-1):
    for y in range(1, ny-1):
        # print("="*70)
        this_tree = grid[x, y]
        # print(f"{x=} {y=} = {this_tree}")
        view_score[x, y] = 1

        # Left, right
        this_score = 0
        for left in range(x-1, -1, -1):
            this_score += 1
            if grid[left, y] < this_tree:
                pass
                # print(f"{left=} {y=} {grid[left, y]=}")
            else:
                break
        view_score[x, y] *= this_score
        # print(f"{this_score=}")

        this_score = 0
        for right in range(x+1, nx):
            this_score += 1
            if grid[right, y] < this_tree:
                pass
                # print(f"{right=} {y=} {grid[right, y]=}")
            else:
                break
        view_score[x, y] *= this_score
        # print(f"{this_score=}")

        # Top, bottom
        this_score = 0
        for top in range(y-1, -1, -1):
            this_score += 1
            if grid[x, top] < this_tree:
                pass
                # print(f"{top=} {y=} {grid[x, top]=}")
            else:
                break
        view_score[x, y] *= this_score
        # print(f"{this_score=}")

        this_score = 0
        for bottom in range(y+1, ny):
            this_score += 1
            if grid[x, bottom] < this_tree:
                pass
                # print(f"{bottom=} {y=} {grid[x, bottom]=}")
            else:
                break
        view_score[x, y] *= this_score
        # print(f"{this_score=}")
        # print()


print(np.max(view_score))

# Both parts together
# [Finished in 355ms]