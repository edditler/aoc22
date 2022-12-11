import math
from collections import deque
import numpy as np

from gmpy2 import mpz

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


class Item:
    def __init__(self, value, initial_monkey):
        super(Item, self).__init__()
        self.value = value
        self.visited_monkeys = [
            initial_monkey,
        ]


monkeys = []
for imonkey, monkey_input in enumerate(monkey_inputs):
    lines = monkey_input.splitlines()
    item_numbers = map(int, lines[1].split(":")[1].split(","))
    items = deque([Item(value, imonkey) for value in item_numbers])
    operation = lines[2].split(":")[1].split("=")[1].strip()
    test = int(lines[3].split("divisible by ")[1])
    if_true = int(lines[4].split()[-1])
    if_false = int(lines[5].split()[-1])

    new_monkey = Monkey(items, operation, test, if_true, if_false)
    monkeys.append(new_monkey)


for iround in range(1, 10001):
    for i, monkey in enumerate(monkeys):
        while len(monkey.items) > 0:
            monkey.inspections += 1
            item = monkey.items.popleft()
            old = item.value
            item.value = eval(monkey.operation)  # Evil, but simple

            if item.value % monkey.test == 0:
                item.visited_monkeys.append(monkey.if_true)
                monkeys[monkey.if_true].items.append(item)
            else:
                item.visited_monkeys.append(monkey.if_false)
                monkeys[monkey.if_false].items.append(item)

    if iround % 500 == 0:
        print(f"After round {iround}:")
        for i, monkey in enumerate(monkeys):
            print(f"Monkey {i}: {monkey.inspections}")

print("=" * 50)

print(f"After round {iround}:")
# all_items = []
# for i, monkey in enumerate(monkeys):
#     for item in monkey.items:
#         item.visited_monkeys = np.array(item.visited_monkeys)
#         all_items.append(item)

# for i, item in enumerate(all_items):
#     print(f"Item {i}:")
#     print(item.visited_monkeys)
#     # print("divisible by 23 or 19")
# a = np.where(item.visited_monkeys == 2)[0]
#     print(np.diff(a))
#     print("=" * 80)

print(sorted([monkey.inspections for monkey in monkeys]))
print(math.prod(sorted([monkey.inspections for monkey in monkeys])[-2:]))
