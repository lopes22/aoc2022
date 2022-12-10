
file1 = open('puzzle9.txt', 'r')
lines = file1.readlines()

visited = set()

knots = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

visited.add((0,0))

for line in lines:
    l = line.strip()

    tokens = l.split(' ')
    direction = tokens[0]
    moves = int(tokens[1])

    for i in range(moves):
        if direction == 'U':
            knots[0][1] = knots[0][1] + 1

        if direction == 'D':
            knots[0][1] = knots[0][1] - 1
                
        if direction == 'L':
            knots[0][0] = knots[0][0] - 1

        if direction == 'R':
            knots[0][0] = knots[0][0] + 1

        for i in range(1, len(knots)):

            h_x = knots[i - 1][0]
            h_y = knots[i - 1][1]
            t_x = knots[i][0]
            t_y = knots[i][1]

            if (t_x, t_y) not in [(h_x, h_y + 1), (h_x + 1, h_y + 1), (h_x - 1, h_y + 1), (h_x, h_y), (h_x, h_y - 1), (h_x - 1, h_y), (h_x + 1, h_y), (h_x - 1, h_y - 1), (h_x + 1, h_y - 1)]:
                if (t_y > h_y):
                    knots[i][1] = knots[i][1] - 1

                if (t_y < h_y): 
                    knots[i][1] = knots[i][1] + 1    

                if (t_x < h_x):
                    knots[i][0] = knots[i][0] + 1
                if (t_x > h_x):
                    knots[i][0] = knots[i][0] - 1

                if (i == len(knots) - 1):
                    visited.add((knots[i][0], knots[i][1]))

print(len(visited))
