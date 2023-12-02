import copy

file1 = open('puzzle18.txt', 'r')

lines = file1.readlines()

droplets = set()
final = set()

max_x = 0
min_x = 10000
max_y = 0
min_y = 10000
max_z = 0
min_z = 10000


for line in lines:
    coords = line.split(',')
    droplets.add((int(coords[0]), int(coords[1]), int(coords[2])))

    max_x = max(max_x, int(coords[0]))
    min_x = min(min_x, int(coords[0]))

    max_y = max(max_y, int(coords[1]))
    min_y = min(min_y, int(coords[1]))

    max_z = max(max_z, int(coords[2]))
    min_z = min(min_z, int(coords[2]))

max_x += 1
min_x -= 1
max_y += 1
min_y -= 1
max_z += 1
min_z -= 1

visited = set()
queue = []
queue.append((min_x, min_y, min_z))
c = 0
while(len(queue) > 0):
    cur = queue.pop(0)
    if (cur in visited):
        continue
    visited.add(cur)
    temp_left = (cur[0] - 1, cur[1], cur[2])
    temp_right = (cur[0] + 1, cur[1], cur[2])
    temp_top = (cur[0], cur[1] + 1, cur[2])
    temp_bottom = (cur[0], cur[1] - 1, cur[2])
    temp_back = (cur[0], cur[1], cur[2] - 1)
    temp_front = (cur[0], cur[1], cur[2] + 1)

    if (temp_left in droplets):
        c += 1

    if (temp_right in droplets):
        c += 1

    if (temp_bottom in droplets):
        c += 1

    if  (temp_top in droplets):
        c += 1

    if (temp_back in droplets):
        c += 1
    
    if (temp_front in droplets):
        c += 1

    if (temp_left[0] >= min_x and temp_left not in droplets):
        queue.append(temp_left)

    if (temp_right[0] <= max_x and temp_right not in droplets):
        queue.append(temp_right)

    if (temp_top[1] <= max_y and temp_top not in droplets):
        queue.append(temp_top)

    if (temp_bottom[1] >= min_y and temp_bottom not in droplets):
        queue.append(temp_bottom)

    if (temp_back[2] >= min_z and temp_back not in droplets):
        queue.append(temp_back)

    if (temp_front[2] <= max_z and temp_front not in droplets):
        queue.append(temp_front)

print(c)