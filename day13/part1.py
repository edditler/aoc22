def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        print(f"Two ints {left} {right}")
        if left < right:
            return True
        elif left == right:
            return None
        elif left > right:
            return False
    elif isinstance(left, list) and isinstance(right, list):
        # If the left list runs out of items first, return True
        #  if both are empty, we can't say anything
        if len(left) == 0 and len(right) == 0:
            return None
        #  if the left list is empty, it will always run out of items first
        elif len(left) == 0:
            return True
        # if the right list is empty, the left will never run out first
        elif len(right) == 0:
            return False

        print(f"Two lists {left} | {right}")
        longer = max(len(left), len(right))
        print(f"The longer list is {longer}")
        for i in range(longer):
            can_compare = i < len(left) and i < len(right)
            if can_compare:
                print(f"We can compare {left[i]}, {right[i]}")
                res = compare(left[i], right[i])
                if res is None:
                    continue
                else:
                    return res
            else:
                print(
                    f"We can't compare at {i}, because {len(left)=} and {len(right)=}"
                )
                return len(left) < len(right)

        # We are at the end and didn't make a decision
        return None
    # exactly one value is an integer
    elif isinstance(left, int) and isinstance(right, list):
        print(f"Mixture {left} | {right}")
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        print(f"Mixture {left} | {right}")
        return compare(left, [right])


with open("input.txt") as f:
    pairs = [a.splitlines() for a in f.read().split("\n\n")]

answer = 0
for ipair, pair in enumerate(pairs):
    print("=" * 10 + f" Pair {ipair+1} " + "=" * 10)
    left = eval(pair[0])
    right = eval(pair[1])
    result = compare(left, right)
    if result is True:
        answer += ipair + 1
    print(left, "|", right, "=>", result)
    print()

print(f"{answer=}")
