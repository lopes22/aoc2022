
file1 = open('puzzle3.txt', 'r')
lines = file1.readlines()

total = 0
line_counter = 0
line_1 = ''
line_2 = ''

for line in lines:
    stripped_line = line.strip()
    line_counter += 1

    if (line_counter == 1):
        line_1 = stripped_line
        continue

    if (line_counter == 2):
        line_2 = stripped_line
        continue

    common = ''
    for i in range(len(stripped_line)):
        for j in range(len(line_1)):
            if (stripped_line[i] == line_1[j]):
                for z in range(len(line_2)):
                    if (stripped_line[i] == line_2[z]):
                        common = stripped_line[i]
                        break
            if (not common == ''):
                break
        if (not common == ''):
            break

    ord_val = ord(common)
    if (ord_val <= ord('Z')):
        total += ord_val - 38
    else:
        total += ord_val - 96

    line_counter = 0
    line_1 = ''
    line_2 = ''

print(total)