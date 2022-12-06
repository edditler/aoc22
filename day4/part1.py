with open("input.txt") as f:
    lines = f.readlines()

n_full = 0
n_overlap = 0

for line in lines:
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))

    if a1 <= b1 and a2 >= b2:
        n_full += 1
        # print(a1, a2, "and", b1, b2)
    elif b1 <= a1 and b2 >= a2:
        n_full += 1
        # print(a1, a2, "and", b1, b2)

    if a1 <= b1 and a2 >= b1:
        n_overlap += 1
    elif b1 <= a1 and b2 >= a1:
        n_overlap += 1

print(n_full)
print(n_overlap)
