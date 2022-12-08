
file1 = open('puzzle7.txt', 'r')
lines = file1.readlines()

amounts = []

def traversal(line_counter):
    size = 0
    while line_counter < len(lines) and lines[line_counter].strip() != '$ cd ..':
        if lines[line_counter].strip() == '$ ls':
            line_counter += 1
            continue

        if 'dir' in lines[line_counter].strip():
            line_counter += 1
            continue

        if 'cd' in lines[line_counter].strip():
            line_counter += 1
            s,l = traversal(line_counter)
            size += s
            line_counter = l
            line_counter += 1
            continue
        
        size += int(lines[line_counter].strip().split(' ')[0])
        line_counter += 1

    amounts.append(size)
    return size, line_counter


s,l = traversal(1)

not_used = 70000000 - s
amounts.sort()
for amt in amounts:
    if amt + not_used > 30000000:
        print(amt)
        break