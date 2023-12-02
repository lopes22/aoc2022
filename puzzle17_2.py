import copy

file1 = open('puzzle17.txt', 'r')
jet_stream = list(file1.readlines()[0])
total_rocks = 1600


rocks = [[(0, 0), (0, 1), (0, 2), (0, 3)],
         [(0,1), (1, 0), (1, 2), (2, 1)],
         [(0,0), (0,1), (0,2), (1,2), (2, 2)],
         [(0,0), (1,0), (2, 0), (3,0)],
         [(0,0), (0,1), (1,0), (1,1)]]

board = [['.','.', '.', '.', '.', '.', '.']]
cur_max_x = 0
rock_counter = 0
cur_rock = None
move_counter = 0

mem = {}

while True:
    move_counter += 1
    if cur_rock == None:
        
        rock_counter += 1

        if rock_counter > total_rocks:
            break
        
        start_x = 4
        if rock_counter == 1:
            start_x -= 1

        cur_rock = copy.deepcopy(rocks[(rock_counter - 1) % len(rocks)])
        
        for i in range(len(cur_rock)):
            cur_rock_piece = cur_rock[i]
            cur_rock[i] = (cur_rock_piece[0] + cur_max_x + start_x, cur_rock_piece[1] + 2)

    jet_direction = jet_stream[(move_counter - 1) % len(jet_stream)]

    can_move = True
    if jet_direction == '>':
        for pos in cur_rock:
            if pos[1] == 6 or (pos[0] <= cur_max_x and board[pos[0]][pos[1] + 1] != '.'):
                can_move = False
                break

        if can_move:
            for i in range(len(cur_rock)):
                cur_rock_piece = cur_rock[i]
                cur_rock[i] = (cur_rock_piece[0], cur_rock_piece[1] + 1)
    else:
        for pos in cur_rock:
            if pos[1] == 0 or (pos[0] <= cur_max_x and board[pos[0]][pos[1] - 1] != '.'):
                can_move = False
                break
        if can_move:
            for i in range(len(cur_rock)):
                cur_rock_piece = cur_rock[i]
                cur_rock[i] = (cur_rock_piece[0], cur_rock_piece[1] - 1)

    can_move_down = True
    for i in range(len(cur_rock)):
        cur_rock_piece = cur_rock[i]
        if cur_rock_piece[0] == 0 or (cur_rock_piece[0] - 1 <= cur_max_x  and board[cur_rock_piece[0] - 1][cur_rock_piece[1]] != '.'):
            can_move_down = False
            break

    if can_move_down:
        for j in range(len(cur_rock)):
            cur_rock_piece = cur_rock[j]
            cur_rock[j] = (cur_rock_piece[0] - 1, cur_rock_piece[1])
    else:
        for j in range(len(cur_rock)):
            cur_rock_piece = cur_rock[j]
            if cur_rock_piece[0] > cur_max_x:
                diff = cur_rock_piece[0] - cur_max_x
                for i in range(diff):
                    board.append(['.', '.', '.', '.', '.', '.', '.'])
                cur_max_x = cur_rock_piece[0]

                r = (rock_counter - 1) % len(rocks)
                s = (move_counter - 1) % len(jet_stream)

                d = 0
                if (r == 4):
                    if (s in mem):
                        d = cur_max_x - mem[s][0]
                        if (d == mem[s][1]):
                            print(d, cur_max_x, rock_counter, rock_counter - mem[s][2])

                    mem[s] = (cur_max_x, d, rock_counter)
            
            board[cur_rock_piece[0]][cur_rock_piece[1]] = '#'
        cur_rock = None

# for x in range(len(board) - 1, -1, -1):
#         print(''.join(board[x]))

print(cur_max_x + 1)