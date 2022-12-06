def letter2priority(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96


def in_all_three(a, b, c):
    for item in a:
        if item in b and item in c:
            return item


with open("input.txt") as f:
    lines = f.readlines()
    nlines = len(lines)

sum_prio = 0
for i_group in range(nlines // 3):
    a, b, c = lines[i_group * 3 : i_group * 3 + 3]
    sum_prio += letter2priority(in_all_three(a, b, c))
print(sum_prio)
