
file1 = open('puzzle4.txt', 'r')
Lines = file1.readlines()

total = 0

for line in Lines:
    stripped_line = line.strip()
    pairs = stripped_line.split(',')

    pair1 = pairs[0].split('-')

    start1 = int(pair1[0])
    end1 = int(pair1[1])

    pair2 = pairs[1].split('-')

    start2 = int(pair2[0])
    end2 = int(pair2[1])

    if start1 <= start2 and end1 >= start2:
        total += 1
        continue

    if start2 <= start1 and end2 >= start1:
        total += 1
        continue

print(total)