file = open('puzzle20.txt', 'r')

lines = file.readlines()

encrypted = []
decrypted = []

key = 811589153

for line in lines:
    encrypted.append(int(line) * key)
    decrypted.append(int(line) * key)

OFFSET = 100000
seen = set()
num_cur_offset = dict()
offsets = dict()
for ind in range(len(encrypted)):
    if (encrypted[ind] in seen):
        if (encrypted[ind] not in num_cur_offset):       
            num_cur_offset[encrypted[ind]] = 1
            offsets[encrypted[ind] + OFFSET] = 1
            encrypted[ind] = encrypted[ind] + OFFSET
            decrypted[ind] = encrypted[ind]
        else:
            num_cur_offset[encrypted[ind]] = num_cur_offset[encrypted[ind]] + 1
            offsets[(OFFSET * num_cur_offset[encrypted[ind]]) + encrypted[ind]] = num_cur_offset[encrypted[ind]]
            encrypted[ind] = encrypted[ind] + (OFFSET * num_cur_offset[encrypted[ind]])
            decrypted[ind] = encrypted[ind]
    else:
        seen.add(encrypted[ind])

for mix in range(10):
    for n in encrypted:
        if (n == 0):
            continue

        cur_i = 0
        actual_n = 0
        if (n not in offsets):
            cur_i = decrypted.index(n)
            actual_n = n
        else:
            cur_i = decrypted.index(n)
            actual_n = (n - (OFFSET * offsets[n]))

        decrypted.pop(cur_i)
        
        new_i = (cur_i + actual_n) % len(decrypted)
        decrypted.insert(new_i, n)


zero_index = decrypted.index(0)

nums = [1000, 2000, 3000]
total = 0
for num in nums:
    i = (num + zero_index) % len(decrypted)
    if (decrypted[i] in offsets):
        total += (decrypted[i] - (OFFSET * offsets[decrypted[i]]))
    else:
        total += decrypted[i]

print(total)