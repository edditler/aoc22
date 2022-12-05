scores = {"X": 1, "Y": 2, "Z": 3}

win_against = {"A": "Y", "B": "Z", "C": "X"}

draw_against = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

lose_against = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}


def one_game(them, me):
    if draw_against[them] == me:
        return 3 + scores[me]
    elif win_against[them] == me:
        return 6 + scores[me]
    else:
        return scores[me]


with open("input1.txt") as f:
    games = f.readlines()

total_score = 0
for game in games:
    them, result = game.split()
    if result == "Y":
        me = draw_against[them]
    elif result == "Z":
        me = win_against[them]
    else:
        me = lose_against[them]
    total_score += one_game(them, me)

print(total_score)
# print(one_game("A", "Y"))
# print(one_game("B", "X"))
# print(one_game("C", "Z"))
