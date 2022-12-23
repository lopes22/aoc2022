
import copy

file1 = open('puzzle16.txt', 'r')
lines = file1.readlines()

tunnles = {}
tunnel_with_f = []
distances = {}

for line in lines:
    tokens = line.strip().split(' ')

    t = tokens[1]
    f = int(tokens[4].split('=')[1].split(';')[0])

    if f > 0:
        tunnel_with_f.append(t)

    tuns = []
    paths = tokens[9:]
    for p in paths:
        tuns.append(p.split(',')[0])

    tunnles[t] = (f, tuns)

for t in tunnel_with_f + ['AA']:
    distances[t] = {}
    for tt in tunnel_with_f:

        q = []
        visited = []
        q.append((t, 0))

        while len(q) > 0:
            qc = q.pop(0)
            c = qc[0]
            p = qc[1]

            if c == tt:
                distances[t][tt] = p
                break

            for o in tunnles[c][1]:
                if o in visited:
                    continue
                visited.append(o)
                q.append((o, p + 1))

mins = 26
stack = [('AA', 0, 0, [])]
max = 0

c = 0
while len(stack) > 0:
    cur = stack.pop()

    cur_t = cur[0]
    cur_total = cur[1]
    cur_min = cur[2]
    open = cur[3]
    c += 1
    if len(open) == len(tunnel_with_f) or cur_min == mins:
        if cur_total > max:
            max = cur_total
        continue

    for t in tunnel_with_f:
        if t in open:
            continue

        d = distances[cur_t][t]

        if (d + cur_min + 1) > mins:
            stack.append((t, cur_total, mins, open))
            break

        m = tunnles[t][0] * (mins - (d + cur_min + 1))
        oo = copy.deepcopy(open)
        oo.append(t)
        stack.append((t, cur_total + m, cur_min + d + 1, oo))

print(max)
print(c)
