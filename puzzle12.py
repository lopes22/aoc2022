
file1 = open('puzzle12.txt', 'r')
lines = file1.readlines()

map = []

for line in lines:
    l = line.strip()
    col = []
    for c in l:
        col.append(c)
    map.append(col)  

graph = {}
start = None
end = None
for r in range(len(map)):
    for c in range(len(map[r])):
        edges = []

        if map[r][c] == 'S':
            start = (r,c)

        if map[r][c] == 'E':
            end = (r,c)
            continue

        cur = map[r][c]
        if r - 1 >= 0 and map[r - 1][c] != 'S':
            if cur == 'S' or (map[r - 1][c] == 'E' and cur == 'z') or ord(cur) + 1 == ord(map[r - 1][c]) or (ord(cur) >= ord(map[r - 1][c]) and ord(map[r - 1][c]) >= ord('a')):
                edges.append((r - 1, c))

        if r + 1 < len(map) and map[r + 1][c] != 'S':
            if cur == 'S' or (map[r + 1][c] == 'E' and cur == 'z') or ord(cur) + 1 == ord(map[r + 1][c]) or (ord(cur) >= ord(map[r + 1][c]) and ord(map[r + 1][c]) >= ord('a')):
                edges.append((r + 1, c))

        if c - 1 >= 0 and map[r][c  - 1] != 'S':
            if cur == 'S' or (map[r][c - 1] == 'E' and cur == 'z') or ord(cur) + 1 == ord(map[r][c - 1]) or (ord(cur) >= ord(map[r][c - 1]) and ord(map[r][c - 1]) >= ord('a')):
                edges.append((r, c - 1))

        if c + 1 < len(map[r]) and map[r][c + 1] != 'S':
            if cur == 'S' or (map[r][c + 1] == 'E' and cur == 'z') or ord(cur) + 1 == ord(map[r][c + 1]) or (ord(cur) >= ord(map[r][c + 1]) and ord(map[r][c + 1]) >= ord('a')):
                edges.append((r, c + 1))

        graph[(r,c)] = edges

print('START: ', start)
print('END: ', end)

visited = set()
paths = {}
q = []
q.append(start)
visited.add(start)
paths[start] = [start]
c = 0
while len(q) > 0:
    cur = q.pop(0)
    if cur == end:

        print("found")
        print(len(paths[cur]) - 1)
        print(paths[cur])
        break

    for v in graph[cur]:
        if v not in visited:
            q.append(v)
            visited.add(v)
            paths[v] = paths[cur] + [v]
