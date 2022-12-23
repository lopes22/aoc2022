
import copy

file1 = open('puzzle16.txt', 'r')
lines = file1.readlines()

tunnles = {}
tunnel_with_f = set()
distances = {}

for line in lines:
    tokens = line.strip().split(' ')

    t = tokens[1]
    f = int(tokens[4].split('=')[1].split(';')[0])

    if f > 0:
        tunnel_with_f.add(t)

    tuns = []
    paths = tokens[9:]
    for p in paths:
        tuns.append(p.split(',')[0])

    tunnles[t] = (f, tuns)

a = copy.deepcopy(tunnel_with_f)
a.add('AA')
for t in a:
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
stack = [('AA', 0, 0, set(), 'AA', 0)]
tmax = 0
opens = []

while len(stack) > 0:
    cur = stack.pop()

    cur_t = cur[0]
    cur_total = cur[1]
    cur_min = cur[2]
    open = cur[3]
    cur_e = cur[4]
    cur_min_e = cur[5]

    if len(open) == len(tunnel_with_f) or cur_min == mins or cur_min_e == mins:
        if cur_total > tmax:
            tmax = cur_total
        continue
    
    s = set()
    for t in tunnel_with_f:
        if t in open:
            continue
        etotals = []
        if len(open) == 0:
            s.add(t)
        for te in tunnel_with_f:
            if te == t or te in open or te in s:
                continue

            de = distances[cur_e][te]
            if (de + cur_min_e + 1) > mins:
                continue

            etotals.append((te, tunnles[te][0] * (mins - (de + cur_min_e + 1)), de + cur_min_e + 1))

        dt = distances[cur_t][t]

        if len(etotals) == 0:
            etotals.append((cur_e, 0, mins))

        for et in etotals:
            if (dt + cur_min + 1) > mins:
                oooo = copy.deepcopy(open)
                if et[0] != cur_e:
                    oooo.add(et[0])
                stack.append((t, cur_total + et[1], mins, oooo, et[0], et[2]))
                continue

            m = tunnles[t][0] * (mins - (dt + cur_min + 1))
            oo = copy.deepcopy(open)
            oo.add(t)
            if et[0] != cur_e:
                oo.add(et[0])
            stack.append((t, cur_total + m + et[1], cur_min + dt + 1, oo, et[0], et[2]))

print(tmax)
