
file1 = open('puzzle1.txt', 'r')
Lines = file1.readlines()

calories = []
calorieCounter = 0
for line in Lines:
    strippedLine = line.strip()
    if strippedLine == '':
        calories.append(calorieCounter)
        calorieCounter = 0
        continue

    calorieCounter += int(strippedLine)

calories.sort(reverse=True)
print(calories[0] + calories[1] + calories[2])