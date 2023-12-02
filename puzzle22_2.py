file = open('puzzle22.txt', 'r')

lines = file.readlines()

rows = []
in_path_mode = False
path = ''
instructions = []

for l in lines:
    if not in_path_mode:
        if (l.strip() == ''):
            in_path_mode = True
            continue
        pieces = list(l[0:len(l) - 1])
        rows.append(pieces)
    else:
        path += l.strip()

cur_i = ''
for i in path:
    if (i.isdigit()):
        cur_i += i
    else:
        instructions.append(cur_i)
        instructions.append(i)
        cur_i = ''

if (cur_i != ''):
    instructions.append(cur_i)

cur_r = 0
cur_c = 50
cur_f = 0

def determine_side(r, c):
    if (r <= 49 and r >= 0 and c >= 50 and c <= 99):
        return 1
    
    if (r <= 49 and r >= 0 and c >= 100 and c <= 149):
        return 2
    
    if (r >= 50 and r <= 99 and c >= 50 and c <= 99):
        return 3
    
    if (r >= 100 and r <= 149 and c <= 49 and c >= 0):
        return 4
    
    if (r >= 100 and r <= 149 and c >= 50 and c <= 99):
        return 5
    
    if (r >= 150 and r <= 199 and c >= 0 and c <= 49):
        return 6

def determine_new_side(cur_side, _r, _c, _f):
    if cur_side == 1: #back
        if _r < 0:
            return (0, _c + 100, 0) # bottom facing right
        if (_c < 50):
            return (0, 149 - _r, 0) # left facing right
        
        return (_f, _r, _c)
        
    if cur_side == 2: # right
        if (_r < 0):
            return (3, 199, _c - 100) # bottom facing up
        if(_r > 49):
            return (2, _c - 50, 99) # top facing left
        if(_c > 149):
            return (2, 149 - _r, 99) # front facing left
        
        return (_f, _r, _c)
        
    if cur_side == 3: # top
        if (_c < 50):
            return (1, 100, _r - 50) # left facing down
        if (_c > 99):
            return (3, 49, _r + 50) # right facing up
        
        return (_f, _r, _c)
        
    if (cur_side == 4): # left
        if (_r < 100):
            return (0, _c  + 50, 50) # top facing right
        if (_c < 0):
            return (0, 149 - _r, 50) #back facing right
        
        return (_f, _r, _c)

    if (cur_side == 5): # front
        if (_r > 149):
            return (2, _c + 100, 49) # bottom facing left
        if (_c > 99):
            return (2, 149 - _r , 149) # right facing left
        
        return (_f, _r, _c)
        
    if (cur_side == 6): # bottom
        if (_r > 199):
            return (1, 0, _c + 100) # right facing down
        if (_c > 49):
            return (3, 149, _r - 100) # front facing up
        if (_c < 0):
            return (1, 0,  _r - 100) # back facing down
        
        return (_f, _r, _c)

for instruction in instructions:
    if (instruction.isdigit()):
        for m in range(int(instruction)):
            if (cur_f == 0):
                new_c = cur_c + 1
                new_r = cur_r
                new_f = cur_f

                s = determine_side(cur_r, cur_c)
                n = determine_new_side(s, new_r, new_c, new_f)

                new_f = n[0]
                new_r = n[1]
                new_c = n[2]

                if (rows[new_r][new_c] == '#'):
                    break

                cur_c = new_c
                cur_r = new_r
                cur_f = new_f
                
            if (cur_f == 1):
                new_r = cur_r + 1
                new_c = cur_c
                new_f = cur_f

                s = determine_side(cur_r, cur_c)
                n = determine_new_side(s, new_r, new_c, new_f)

                new_f = n[0]
                new_r = n[1]
                new_c = n[2]

                if (rows[new_r][new_c] == '#'):
                    break

                cur_r = new_r
                cur_c = new_c
                cur_f = new_f

            if (cur_f == 2):
                new_c = cur_c - 1
                new_r = cur_r
                new_f = cur_f

                s = determine_side(cur_r, cur_c)
                n = determine_new_side(s, new_r, new_c, new_f)

                new_f = n[0]
                new_r = n[1]
                new_c = n[2]

                if (rows[new_r][new_c] == '#'):
                    break

                cur_c = new_c
                cur_r = new_r
                cur_f = new_f

            if (cur_f == 3):
                new_r = cur_r - 1
                new_c = cur_c
                new_f = cur_f

                s = determine_side(cur_r, cur_c)
                n = determine_new_side(s, new_r, new_c, new_f)

                new_f = n[0]
                new_r = n[1]
                new_c = n[2]
                    
                if (rows[new_r][new_c] == '#'):
                    break

                cur_r = new_r
                cur_c = new_c
                cur_f = new_f
            
    else:
        if (instruction == 'R'):
            cur_f = (cur_f + 1) % 4
        else:
            cur_f = (cur_f - 1) % 4

total = 1000 * (cur_r + 1) + 4 * (cur_c + 1) + cur_f

print(cur_r, cur_c, cur_f)
print(total)

# print(determine_new_side(1, -1, 50, 3) == (0, 150, 0))
# print(determine_new_side(1, -1, 99, 3) == (0, 199, 0))

# print(determine_new_side(1, 0, 49, 2) == (0, 149, 0))
# print(determine_new_side(1, 49, 49, 2) == (0, 100, 0))

# print(determine_new_side(2, -1, 100, 3) == (3, 199, 0))
# print(determine_new_side(2, -1, 149, 3) == (3, 199, 49))

# print(determine_new_side(2, 50, 100, 1) == (2, 50, 99))
# print(determine_new_side(2, 50, 149, 1) == (2, 99, 99))

# print(determine_new_side(2, 0, 150, 0) == (2, 149, 99))
# print(determine_new_side(2, 49, 150, 0) == (2, 100, 99))

# print(determine_new_side(5, 100, 100, 0) == (2, 49, 149))
# print(determine_new_side(5, 149, 100, 0) == (2, 0, 149))

# print(determine_new_side(3, 50, 100, 0) == (3, 49, 100))
# print(determine_new_side(3, 99, 100, 0) == (3, 49, 149))

# print(determine_new_side(6, 200, 0, 1) == (1, 0, 100))
# print(determine_new_side(6, 200, 49, 1) == (1, 0, 149))

# print(determine_new_side(4, 100, -1, 2) == (0, 49, 50))
# print(determine_new_side(4, 149, -1, 2) == (0, 0, 50))

# print(determine_new_side(6, 150, -1, 2) == (1, 0, 50))
# print(determine_new_side(6, 199, -1, 2) == (1, 0, 99))