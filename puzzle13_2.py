
file1 = open('puzzle13.txt', 'r')
lines = file1.readlines()

packets = []
for i in range(0, len(lines), 3):
    p1 = eval(lines[i].strip())
    p2 = eval(lines[i + 1].strip())

    packets.append(p1)
    packets.append(p2)


#bubble sort
for b in range(len(packets)):
    for n in range(0, len(packets) - b - 1):
        p1 = packets[n]
        p2 = packets[n + 1]
        stack = []
        stack.append((p1, p2))

        while len(stack) > 0:
            cur = stack.pop()

            if len(cur[0]) == 0 and len(cur[1]) > 0:
                stack.clear()
                break

            for j in range(len(cur[0])):
                if j > (len(cur[1]) - 1):
                    packets[n], packets[n+1] = packets[n+1], packets[n]
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
                    packets[n], packets[n+1] = packets[n+1], packets[n]
                    stack.clear()
                    break
                else:
                    stack.clear()
                    break


first = 0
second = 0
for p in range(len(packets)):
    print(packets[p])
    if len(packets[p]) == 1 and type(packets[p][0]) is list and len(packets[p][0]) == 1 and packets[p][0][0] == 2:
        first = p + 1

    if len(packets[p]) == 1 and type(packets[p][0]) is list and len(packets[p][0]) == 1 and packets[p][0][0] == 6:
        second = p + 1

print(first * second)
