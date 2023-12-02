
import copy

file1 = open('puzzle16.txt', 'r')
lines = file1.readlines()

tunnles = {}
total_with_f = 0

for line in lines:
    tokens = line.strip().split(' ')

    t = tokens[1]
    f = int(tokens[4].split('=')[1].split(';')[0])

    if f > 0:
        total_with_f += 1

    tuns = []
    paths = tokens[9:]
    for p in paths:
        tuns.append(p.split(',')[0])

    tunnles[t] = (f, tuns)

mins = 30

stack = []
stack.append((1, [], 0, 'AA', 'AA'))
max = 0

while len(stack) > 0:

    cur = stack.pop()

    m = cur[0]
    open = cur[1]
    total = cur[2]
    tunnel = cur[3]
    path = cur[4]

    if (m == mins):
        if total > max:
            max = total
        continue

    if len(open) == total_with_f:
        if total > max:
            max = total
            print(max,path)
        continue

    if tunnel not in open and tunnles[tunnel][0] > 0:
        new_total = total + (tunnles[tunnel][0] * (mins - m))
        oo = copy.deepcopy(open)
        oo.append(tunnel)
        stack.append((m + 1, oo, new_total, tunnel, path + ',,'))

    others = tunnles[tunnel][1]

    for o in others:
        v = []
        cycle = False
        p = copy.deepcopy(path)
        p += o
        for i in range(0, len(p), 2):
            yy = p[i] + p[i + 1]
            if yy == ',,':
                v = []
                continue
            else:
                if yy in v:
                    cycle = True
                    break
                else:
                    v.append(yy)
        if cycle:
            continue

        stack.append((m + 1, open, total, o, p))  

print(max)


