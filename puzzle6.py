
file1 = open('puzzle6.txt', 'r')
lines = file1.readlines()

line = lines[0]
c = 0
buffer = []
for l in line:
    if len(buffer) == 14:
        break

    if l in buffer:
        buffer = buffer[buffer.index(l) + 1:]

    buffer.append(l)
    c += 1

print(c)