
file1 = open('puzzle15.txt', 'r')
lines = file1.readlines()

coords = []
row = set()
y_find = 2000000

max_x = 0
min_x = 0

for line in lines:
    tokens = line.strip().split(' ')
    sx = int(tokens[2].split('=')[1].split(',')[0])
    sy = int(tokens[3].split('=')[1].split(':')[0])

    if sx > max_x:
        max_x = sx

    if sx < min_x:
        min_x = sx

    bx = int(tokens[8].split('=')[1].split(',')[0])
    by = int(tokens[9].split('=')[1])

    if bx > max_x:
        max_x = bx

    if bx < min_x:
        min_x = bx

    coords.append([(sx,sy), (bx,by)])

for coord_pair in coords:
    s = coord_pair[0]
    b = coord_pair[1]

    print(s,b)

    x_dist = abs(s[0] - b[0])
    y_dist = abs(s[1] - b[1])

    distance = x_dist + y_dist

    if s[1] < y_find and s[1] + distance >= y_find:
        dis_to_y = y_find - s[1]
        r = distance - dis_to_y

        for i in range(r + 1):
            row.add(s[0] - i)
            row.add(s[0] + i)

    if s[1] > y_find and s[1] - distance <= y_find:
        dis_to_y = s[1] - y_find
        r = distance - dis_to_y

        for i in range(r + 1):
            row.add(s[0] - i)
            row.add(s[0] + i)

for cc in coords:
    s = cc[0]
    b = cc[1]

    if s[1] == y_find and s[0] in row:
        row.remove(s[0])

    if b[1] == y_find and b[0] in row:
        row.remove(b[0])

print(len(row))