def letter2priority(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96


def split_rucksack(content):
    compartment_a = content[: len(content) // 2]
    compartment_b = content[len(content) // 2 :]
    return (compartment_a, compartment_b)


def appear_in_both(a, b):
    for item in a:
        if item in b:
            return item


with open("input.txt") as f:
    lines = f.readlines()

sum_prio = 0
for rucksack in lines:
    sum_prio += letter2priority(appear_in_both(*split_rucksack(rucksack)))
print(sum_prio)
