import math
from collections import deque

with open("input.txt") as f:
    monkey_inputs = f.read().split("\n\n")


class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        super(Monkey, self).__init__()
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0


monkeys = []
all_prime = True
for monkey_input in monkey_inputs:
    lines = monkey_input.splitlines()
    items = deque(map(int, lines[1].split(":")[1].split(",")))
    operation = lines[2].split(":")[1].split("=")[1].strip()
    test = int(lines[3].split("divisible by ")[1])
    if_true = int(lines[4].split()[-1])
    if_false = int(lines[5].split()[-1])

    new_monkey = Monkey(items, operation, test, if_true, if_false)
    monkeys.append(new_monkey)

for iround in range(1, 21):
    for i, monkey in enumerate(monkeys):
        while len(monkey.items) > 0:
            monkey.inspections += 1
            old = monkey.items.popleft()
            new = math.floor(int(eval(monkey.operation)) / 3)  # Evil, but simple
            if new % monkey.test == 0:
                monkeys[monkey.if_true].items.append(new)
            else:
                monkeys[monkey.if_false].items.append(new)

    if iround % 100 == 0:
        print(f"After round {iround+1}:")
        # for i, monkey in enumerate(monkeys):
        # print(f"Monkey {i}: {list(monkey.items)}")
        for i, monkey in enumerate(monkeys):
            print(f"Monkey {i}: {monkey.inspections}")

print("=" * 50)


print(math.prod(sorted([monkey.inspections for monkey in monkeys])[-2:]))
