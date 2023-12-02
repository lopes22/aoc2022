file = open('puzzle21.txt', 'r')

lines = file.readlines()

equation = ''
stack = []
monkeys = dict()
for line in lines:
    l = line.strip()
    s = l.split(': ')

    if s[0] == 'root':
        #equation = s[1]
        #root_s = equation.split(' ')
        root_s = s[1].split(' ')
        stack.append(root_s[0])
        #stack.append(root_s[2])
        equation = root_s[0]
    else:
        monkeys[s[0]] = s[1]

while(len(stack) > 0):
    cur = stack.pop()
    v = monkeys[cur]

    if (cur == 'humn'):
        continue

    if (v.isdigit()):
        equation = equation.replace(cur, v)
    else:
        equation = equation.replace(cur, '(' + v + ')')
        cur_s = v.split(' ')
        stack.append(cur_s[0])
        stack.append(cur_s[2])

#print(equation)
#print(eval(equation))

inc = 10000000000
i = 10000000000
while True:
    new_e = equation.replace('humn', str(i))
    result = int(eval(new_e))

    if (result > 28379346560301):
        i += inc
        continue

    if (result < 28379346560301):
        old_inc = inc
        inc = inc // 10
        inc = max(inc, 1)
        i -= old_inc
        continue

    if (result == 28379346560301):
        print(i)
        break
