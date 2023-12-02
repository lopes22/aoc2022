file = open('puzzle22.txt', 'r')

lines = file.readlines()

rows = []
in_path_mode = False
path = ''
instructions = []

for l in lines:
    if not in_path_mode:
        if (l.strip() == ''):
            in_path_mode = True
            continue
        pieces = list(l[0:len(l) - 1])
        rows.append(pieces)
    else:
        path += l.strip()

cur_i = ''
for i in path:
    if (i.isdigit()):
        cur_i += i
    else:
        instructions.append(cur_i)
        instructions.append(i)
        cur_i = ''

if (cur_i != ''):
    instructions.append(cur_i)

cur_r = 0
cur_c = 0
cur_f = 0

for c in range(len(rows[0])):
    if (rows[0][c] == '.'):
        cur_c = c
        break

for instruction in instructions:
    if (instruction.isdigit()):
        for m in range(int(instruction)):
            if (cur_f == 0):
                new_c = cur_c + 1
                if(new_c > len(rows[cur_r]) - 1):
                    new_c = 0
                    while(True):
                        if (rows[cur_r][new_c] == ' '):
                            new_c += 1
                            continue
                        if (rows[cur_r][new_c] == '.'):
                            break
                        if (rows[cur_r][new_c] == '#'):
                            break

                if (rows[cur_r][new_c] == '#'):
                    break

                cur_c = new_c
                
            if (cur_f == 1):
                new_r = cur_r + 1
                if(new_r > (len(rows) - 1) or cur_c > (len(rows[new_r]) - 1) or rows[new_r][cur_c] == ' '):
                    new_r = 0
                    while(True):
                        if(cur_c > (len(rows[new_r]) - 1)):
                            new_r += 1
                            continue
                        if (rows[new_r][cur_c] == ' '):
                            new_r += 1
                            continue
                        if (rows[new_r][cur_c] == '.'):
                            break
                        if (rows[new_r][cur_c] == '#'):
                            break

                if (rows[new_r][cur_c] == '#'):
                    break

                cur_r = new_r

            if (cur_f == 2):
                new_c = cur_c - 1
                if(new_c < 0 or rows[cur_r][new_c] == ' '):
                    new_c = len(rows[cur_r]) - 1
                    while(True):
                        if (rows[cur_r][new_c] == ' '):
                            new_c -= 1
                            continue
                        if (rows[cur_r][new_c] == '.'):
                            break
                        if (rows[cur_r][new_c] == '#'):
                            break

                if (rows[cur_r][new_c] == '#'):
                    break

                cur_c = new_c

            if (cur_f == 3):
                new_r = cur_r - 1
                if(new_r < 0 or cur_c > (len(rows[new_r]) - 1) or rows[new_r][cur_c] == ' '):
                    new_r = len(rows) - 1
                    while(True):
                        if(cur_c > (len(rows[new_r]) - 1)):
                            new_r -= 1
                            continue
                        if (rows[new_r][cur_c] == ' '):
                            new_r -= 1
                            continue
                        if (rows[new_r][cur_c] == '.'):
                            break
                        if (rows[new_r][cur_c] == '#'):
                            break

                if (rows[new_r][cur_c] == '#'):
                    break

                cur_r = new_r
            
    else:
        if (instruction == 'R'):
            cur_f = (cur_f + 1) % 4
        else:
            cur_f = (cur_f - 1) % 4

total = 1000 * (cur_r + 1) + 4 * (cur_c + 1) + cur_f

print(cur_r, cur_c, cur_f)
print(total)