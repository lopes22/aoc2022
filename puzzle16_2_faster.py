
import copy

file1 = open('puzzle16_2.txt', 'r')
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

a = copy.deepcopy(tunnel_with_f)
a.append('AA')
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

bitmap = {}
for i in range(len(tunnel_with_f)):
    bitmap[tunnel_with_f[i]] = i

most = (2 ** len(tunnel_with_f)) - 1
mins = 26
stack = [('AA', 0, 0, 0, 'AA', 0)]
tmax = 0
mem = {}

while len(stack) > 0:
    cur = stack.pop()

    cur_t = cur[0]
    cur_total = cur[1]
    cur_min = cur[2]
    open = cur[3]
    cur_e = cur[4]
    cur_min_e = cur[5]

    if open > 0:
        if open not in mem:
            mem[open] = (cur_total, cur_min)
        else:
            if mem[open][0] > cur_total and max(cur_min, cur_min_e) > mem[open][1]:
                continue
            else:
                mem[open] = (cur_total, max(cur_min, cur_min_e))


    if open == most or (cur_min == mins and cur_min_e == mins):
        if cur_total > tmax:
            tmax = cur_total
        continue
    
    s = set()
    for t in tunnel_with_f:
        tbit_p = bitmap[t]
        if open & (1 << tbit_p):
            continue
        etotals = []
        if open == 0:
            s.add(t)
        for te in tunnel_with_f:
            ebit_p = bitmap[te]
            if te == t or (open & (1 << ebit_p)) or te in s:
                continue

            de = distances[cur_e][te]
            if (de + cur_min_e + 1) > mins:
                continue

            etotals.append((te, tunnles[te][0] * (mins - (de + cur_min_e + 1)), de + cur_min_e + 1))

        dt = distances[cur_t][t]

        if len(etotals) == 0:
            etotals.append((cur_e, 0, mins))

        for et in etotals:
            ooo = open
            if (dt + cur_min + 1) > mins:
                if et[0] != cur_e:
                    bit_p_e = bitmap[et[0]]
                    ooo = ooo | (2 ** bit_p_e)
                stack.append((t, cur_total + et[1], mins, ooo, et[0], et[2]))
                continue

            m = tunnles[t][0] * (mins - (dt + cur_min + 1))
            bit_p_t = bitmap[t]
            ooo = ooo | (2 ** bit_p_t)
            if et[0] != cur_e:
                bit_p_e = bitmap[et[0]]
                ooo = ooo | (2 ** bit_p_e)
            stack.append((t, cur_total + m + et[1], cur_min + dt + 1, ooo, et[0], et[2]))
print(tmax)
