
file1 = open('puzzle13.txt', 'r')
lines = file1.readlines()

correct_pairs = []
for i in range(0, len(lines), 3):
    p1 = eval(lines[i].strip())
    p2 = eval(lines[i + 1].strip())

    stack = []
    stack.append((p1, p2))
    correct = True
    while len(stack) > 0:
        cur = stack.pop()

        if len(cur[0]) == 0 and len(cur[1]) > 0:
            stack.clear()
            break

        for j in range(len(cur[0])):
            if j > (len(cur[1]) - 1):
                correct = False
                stack.clear()
                break
            
            if type(cur[0][j]) is list and type(cur[1][j]) is not list:
                stack.append((cur[0][j + 1:], cur[1][j + 1:]))
                stack.append((cur[0][j], [cur[1][j]]))
                break

            if type(cur[0][j]) is not list and type(cur[1][j]) is list:
                stack.append((cur[0][j + 1:], cur[1][j + 1:]))
                stack.append(([cur[0][j]], cur[1][j]))
                break

            if type(cur[0][j]) is list and type(cur[1][j]) is list:
                stack.append((cur[0][j + 1:], cur[1][j + 1:]))
                stack.append((cur[0][j], cur[1][j]))
                break

            if cur[0][j] == cur[1][j]:
                if j == (len(cur[0]) - 1) and len(cur[1]) > len(cur[0]):
                    stack.clear()
                    break
                else:
                    continue

            if cur[0][j] > cur[1][j]:
                correct = False
                stack.clear()
                break
            else:
                stack.clear()
                break

    if correct:
        correct_pairs.append((i // 3) + 1)

print(correct_pairs)
total = 0
for pair in correct_pairs:
    total += pair

print(total)


