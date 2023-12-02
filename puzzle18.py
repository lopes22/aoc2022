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

not_possible = set()
possible = set()
for d in droplets:
    final.add(d)

    temp_left = d
    tl = []
    while(True):
        if (temp_left[0] == min_x):
            not_possible.update(tl)
            tl.clear()
            break

        temp_left = (temp_left[0] - 1, temp_left[1], temp_left[2])

        if (temp_left not in droplets):
            tl.append(temp_left)
        elif (temp_left in not_possible):
            tl.clear()
            break
        else:
            break
    
    temp_right = d
    tr = []
    while(True):
        if (temp_right[0] == max_x or temp_right in not_possible):
            not_possible.update(tr)
            tr.clear()
            break

        temp_right = (temp_right[0] + 1, temp_right[1], temp_right[2])

        if (temp_right not in droplets):
            tr.append(temp_right)
        elif (temp_right in not_possible):
            tr.clear()
            break
        else:
            break
    
    temp_top = d
    tt = []
    while(True):
        if (temp_top[1] == max_y):
            not_possible.update(tt)
            tt.clear()
            break

        temp_top = (temp_top[0], temp_top[1] + 1, temp_top[2])

        if (temp_top not in droplets):
            tt.append(temp_top)
        elif (temp_top in not_possible):
            tt.clear()
            break
        else:
            break

    temp_bottom = d
    tb = []
    while(True):
        if (temp_bottom[1] == min_y):
            not_possible.update(tb)
            tb.clear()
            break
    
        temp_bottom = (temp_bottom[0], temp_bottom[1] - 1, temp_bottom[2])

        if (temp_bottom not in droplets):
            tb.append(temp_bottom)
        elif (temp_bottom in not_possible):
            tb.clear()
            break
        else:
            break

    temp_back = d
    tbb = []
    while(True):  
        if (temp_back[2] == min_z):
            not_possible.update(tbb)
            tbb.clear()
            break

        temp_back = (temp_back[0], temp_back[1], temp_back[2] - 1)

        if (temp_back not in droplets):
            tbb.append(temp_back)
        elif (temp_back in not_possible):
            tbb.clear()
            break
        else:
            break

    temp_front = d
    tf = []
    while(True):
        if (temp_front[2] == max_z):
            not_possible.update(tf)
            tf.clear()
            break

        temp_front = (temp_front[0], temp_front[1], temp_front[2] + 1)
        
        if (temp_front not in droplets):
            tf.append(temp_front)
        elif (temp_front in not_possible):
            tf.clear()
            break
        else:
            break

    possible.update(tl)
    possible.update(tf)
    possible.update(tbb)
    possible.update(tb)
    possible.update(tr)
    possible.update(tt)


f = possible - not_possible
final.update(f)

total_uncovered = 0
for droplet in final:
    left = (droplet[0] - 1, droplet[1], droplet[2])

    if (left not in final):
        total_uncovered += 1
    
    right = (droplet[0] + 1, droplet[1], droplet[2])

    if (right not in final):
        total_uncovered += 1
    
    top = (droplet[0], droplet[1] + 1, droplet[2])

    if (top not in final):
        total_uncovered += 1

    bottom = (droplet[0], droplet[1] - 1, droplet[2])

    if (bottom not in final):
        total_uncovered += 1
    
    back = (droplet[0], droplet[1], droplet[2] - 1)

    if (back not in final):
        total_uncovered += 1

    front = (droplet[0], droplet[1], droplet[2] + 1)
    
    if (front not in final):
        total_uncovered += 1

print(total_uncovered)