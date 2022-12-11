
file1 = open('puzzle10.txt', 'r')
lines = file1.readlines()

crt = []

for i in range(6):
    c = []
    for j in range(40):
        c.append('.')
    crt.append(c)

cycle_counter = 1
reg = 1
for line in lines:
    instruction = line.strip()
    instruction_cycle_counter = 0

    while True:
        sprite = [reg - 1, reg, reg + 1]

        crt_r = (cycle_counter - 1) // 40
        crt_c = (cycle_counter - 1) - (40 * crt_r)
        for pos in sprite:
            if pos < 0 or pos > 40:
                continue

            if crt_c == pos:
                crt[crt_r][crt_c] = '#'
                break

        if instruction == 'noop':
            cycle_counter += 1
            break
        else:
            add = int(instruction.split()[1])

            instruction_cycle_counter += 1
            cycle_counter += 1

            if instruction_cycle_counter == 2:
                reg += add
                break

for i in range(len(crt)):
    l = ''
    for j in range(len(crt[i])):
        l += crt[i][j]
    print(l)