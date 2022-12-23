
file1 = open('puzzle15.txt', 'r')
lines = file1.readlines()

coords = []

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

found = False
for yspace in range(4000000 + 1):
    row = []
    if found:
        break
    print(yspace)
    y_find = yspace
    for coord_pair in coords:
        s = coord_pair[0]
        b = coord_pair[1]

        x_dist = abs(s[0] - b[0])
        y_dist = abs(s[1] - b[1])

        distance = x_dist + y_dist

        if s[1] <= y_find and s[1] + distance >= y_find:
            dis_to_y = y_find - s[1]
            r = distance - dis_to_y

            if s[0] + r <= 4000000 and s[0] - r >= 0:
                row.append((s[0] - r, s[0] + r))
            elif s[0] + r <= 4000000:
                row.append((0, s[0] + r))
            else:
                row.append((s[0] - r, 4000000))

        if s[1] > y_find and s[1] - distance <= y_find:
            dis_to_y = s[1] - y_find
            r = distance - dis_to_y

            if s[0] + r <= 4000000 and s[0] - r >= 0:
                row.append((s[0] - r, s[0] + r))
            elif s[0] + r <= 4000000:
                row.append((0, s[0] + r))
            else:
                row.append((s[0] - r, 4000000))

    row.sort()
    mmin = row[0][0]
    mmax = row[0][1]
    for t in range(1, len(row)):
        if row[t][0] <= mmax: 
            if row[t][1] > mmax:
                mmax = row[t][1]

    if mmin != 0 or mmax != 4000000:
        if mmin != 0:
            print(((mmin - 1) * 4000000) + y_find)
        else:
            print(((mmax + 1) * 4000000) + y_find)
        found = True