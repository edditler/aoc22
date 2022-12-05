scores = {"X": 1, "Y": 2, "Z": 3}

win_against = {"A": "Y", "B": "Z", "C": "X"}
draw_against = {
    "A": "X",
    "B": "Y",
    "C": "Z",
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
    them, me = game.split()
    total_score += one_game(them, me)

print(total_score)
# print(one_game("A", "Y"))
# print(one_game("B", "X"))
# print(one_game("C", "Z"))
