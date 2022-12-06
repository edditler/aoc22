with open("input.txt") as f:
    puzzle = f.read()

# puzzle = "nppdvjthqldpwncqszvftbrmjlhg"
# print(puzzle)


def has_duplicates(sequence):
    for i, s in enumerate(sequence):
        if s in sequence[i + 1 :]:
            return True
    return False


def find_start(puzzle):
    for i in range(0, len(puzzle)):
        sequence = puzzle[i : i + 4]
        # print(i, sequence)
        if not has_duplicates(sequence):
            return (i + 4, sequence)
    # return (i, sequence)


print(find_start("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
print("=" * 20)
print(find_start("bvwbjplbgvbhsrlpgdmjqwftvncz"))
print("=" * 20)
print(find_start("nppdvjthqldpwncqszvftbrmjlhg"))
print("=" * 20)
print(find_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print("=" * 20)
print(find_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
print("=" * 20)
print(find_start(puzzle))
print("=" * 20)
