
file1 = open('puzzle1.txt', 'r')
lines = file1.readlines()

calories = []
calorie_counter = 0
for line in lines:
    stripped_line = line.strip()
    if stripped_line == '':
        calories.append(calorie_counter)
        calorie_counter = 0
        continue

    calorie_counter += int(stripped_line)

calories.sort(reverse=True)
print(calories[0] + calories[1] + calories[2])