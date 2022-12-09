
file1 = open('puzzle8.txt', 'r')
lines = file1.readlines()

grid = []
for line in lines:
    row = []
    for i in range(len(line.strip())):
        row.append(int(line.strip()[i]))
    grid.append(row)

score = -1
for i in range(len(grid)):
    for j in range(len(grid[i])):

        if i == 0:
            continue

        if i == len(grid) - 1:
            continue

        if j == 0:
            continue

        if j == len(grid[i]) - 1:
            continue

        tree = grid[i][j]

        b_score = 0
        l_score = 0
        t_score = 0
        r_score = 0

        for b in range(i + 1, len(grid)):
            if grid[b][j] < tree:
                b_score += 1
            else:
                b_score += 1
                break

        for l in range(j + 1, len(grid[i])):
            if grid[i][l] < tree:
                l_score += 1
            else:
                l_score += 1
                break

        for t in range(i - 1, -1, -1):
            if grid[t][j] < tree:
                t_score += 1
            else:
                t_score += 1
                break

        for r in range(j - 1, -1, -1):
            if grid[i][r] < tree:
                r_score += 1
            else:
                r_score += 1
                break

        s = b_score * t_score * r_score * l_score

        if s > score:
            score = s

print(score)
