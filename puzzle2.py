
file1 = open('puzzle2.txt', 'r')
Lines = file1.readlines()

score_map = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

total_score = 0
for line in Lines:
    strippedLine = line.strip()

    total_score += score_map[strippedLine]

print(total_score)