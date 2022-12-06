
file1 = open('puzzle5.txt', 'r')
lines = file1.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]

for line in lines[:9]:
    stripped_line = line.strip()

    for i in range(1, len(stripped_line), 4):
        if (stripped_line[i] != ' '):
            stack = stacks[(i - 1) // 4]
            stack.insert(0, stripped_line[i])

for line in lines[10:]:
    stripped_line = line.strip()
    tokens = stripped_line.split(' ')

    num = int(tokens[1])
    from_stack_num = int(tokens[3])
    to_stack_num = int(tokens[5])

    from_stack = stacks[from_stack_num - 1]
    to_stack = stacks[to_stack_num - 1]

    for i in range(num, 0, -1):
        box = from_stack.pop(i * -1)
        to_stack.append(box)

stack_final = ''
for i in range(9):
    stack_final += stacks[i][-1]

print(stack_final)

    




