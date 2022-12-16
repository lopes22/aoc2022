
file1 = open('puzzle14.txt', 'r')
lines = file1.readlines()

map = []
rock_lines = []

max_x = 0
max_y = 0
min_y = 10000
for line in lines:
    rocks = line.strip().split(' -> ')
    temp = []
    for rock in rocks:
        p = rock.split(',')
        y = int(p[0])
        x = int(p[1])

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

        if y < min_y:
            min_y = y

        temp.append((x,y))
    rock_lines.append(temp)

y_offset = 250
xx = max_x + 3
yy = (max_y - min_y) + 1 + 500

for x in range(xx):
    temp = []
    for y in range(yy):
        temp.append('.')
    map.append(temp)

for f in range(len(map[xx - 1])):
    map[xx - 1][f] = 'R'

for rock_line in rock_lines:
    for i in range(len(rock_line) - 1):
        coord1 = rock_line[i]
        coord2 = rock_line[i + 1]
        print(coord1, coord2)
        if coord1[0] == coord2[0]:
            x = coord1[0]
            if coord1[1] > coord2[1]:
                for j in range((coord1[1] - coord2[1]) + 1):
                    y = ((coord2[1] - min_y) + y_offset) + j
                    map[x][y] = "R"
            else:
                for j in range((coord2[1] - coord1[1]) + 1):
                    y = (coord1[1] - min_y) + y_offset + j
                    map[x][y] = "R"            
        else:
            y = (coord1[1] - min_y)  + y_offset
            if coord2[0] > coord1[0]:
                for j in range((coord2[0] - coord1[0]) + 1):
                    x = coord1[0] + j
                    map[x][y] = "R"
            else:
                  for j in range((coord1[0] - coord2[0]) + 1):
                    x = coord2[0] + j
                    map[x][y] = "R"              

print("X: ", xx)
print("Y: ", yy)
print("LINES: ", len(rock_lines))

for ml in map:
    print(''.join(ml))

sand_counter = 0
abyss = True
while map[0][(500 - min_y) + y_offset] == '.':
    sand_counter += 1
    print("COUNTER: ", sand_counter)
    cur_sand_x = 0
    cur_sand_y = (500 - min_y) + y_offset

    print("START", cur_sand_x,cur_sand_y)
    placed = False
    while True:
        print(cur_sand_x,cur_sand_y)
        if map[cur_sand_x + 1][cur_sand_y] == '.':
            cur_sand_x += 1
            continue

        if map[cur_sand_x + 1][cur_sand_y - 1] == '.':
            cur_sand_x += 1
            cur_sand_y -= 1
            continue

        if map[cur_sand_x + 1][cur_sand_y + 1] == '.':
            cur_sand_x += 1
            cur_sand_y += 1
            continue

        map[cur_sand_x][cur_sand_y] = 'S'
        break

print(sand_counter)

for ml in map:
    print(''.join(ml))


        

