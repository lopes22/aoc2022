
import math


file1 = open('puzzle11.txt', 'r')
lines = file1.readlines()

monkey_items = []
monkey_op = []
monkey_test = []
monkey_true = []
monkey_false = []

monkey_inspection = []

for i in range(1, len(lines), 7):
    items = lines[i].strip().split(':')[1].split(',')
    for j in range(len(items)):
        items[j] = int(items[j])
    monkey_items.append(items)

    monkey_op.append(lines[i + 1].strip().split('=')[1])

    monkey_test.append(int(lines[i + 2].strip().split('by')[1]))

    monkey_true.append(int(lines[i + 3].strip().split('monkey')[1]))

    monkey_false.append(int(lines[i + 4].strip().split('monkey')[1]))

    monkey_inspection.append(0)

m = math.lcm(*monkey_test)
print(m)
for round in range(10000):
    for monkey_i in range(len(monkey_items)):

        while len(monkey_items[monkey_i]) > 0:
            monkey_inspection[monkey_i] = monkey_inspection[monkey_i] + 1

            worry_item_amount = monkey_items[monkey_i].pop(0)
            
            worry_item_amount = eval(monkey_op[monkey_i].replace('old', str(worry_item_amount)))

            if worry_item_amount % monkey_test[monkey_i] == 0:
                monkey_items[monkey_true[monkey_i]].append(worry_item_amount % m)
            else:
                monkey_items[monkey_false[monkey_i]].append(worry_item_amount % m)

monkey_inspection.sort(reverse=True)
print(monkey_inspection[0] * monkey_inspection[1])
