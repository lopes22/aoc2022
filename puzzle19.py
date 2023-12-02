import copy

file1 = open('puzzle19.txt', 'r')

lines = file1.readlines()

blue_prints = []

for line in lines:
    parts = line.split(' ')

    id = int(parts[1].split(':')[0])
    ore_bot = int(parts[6])
    clay_bot = int(parts[12])
    obsidian_bot = (int(parts[18]), int(parts[21]))
    geode_bot = (int(parts[27]), int(parts[30]))

    blue_prints.append((id, ore_bot, clay_bot, obsidian_bot, geode_bot))

def game(ore_bots, clay_bots, obsidian_bots, geode_bots, ore, clay, obsidian, geodes, day, blue_print, idle_count):
    if (day == 32):
        return geodes + geode_bots
    
    more = max(blue_print[2], blue_print[3][0], blue_print[4][0])
    
    if (idle_count > more):
        return 0
    
    if (day == 6 and ore_bots == 1 and clay_bots == 0):
        return 0

    if (ore >= blue_print[4][0] and obsidian >= blue_print[4][1]):
        return game(ore_bots, clay_bots , obsidian_bots, geode_bots + 1, ore + ore_bots - blue_print[4][0], clay + clay_bots, obsidian + obsidian_bots - blue_print[4][1], geodes + geode_bots, day + 1, blue_print, 0)
    
    obsidian_need = blue_print[4][1] - obsidian_bots

    if (ore >= blue_print[3][0] and clay >= blue_print[3][1] and obsidian_need > 0):
        obsidian_bot_path = game(ore_bots, clay_bots , obsidian_bots + 1, geode_bots, ore + ore_bots - blue_print[3][0], clay + clay_bots - blue_print[3][1], obsidian + obsidian_bots, geodes + geode_bots, day + 1, blue_print, 0)
        do_nothing_path_1 = game(ore_bots, clay_bots, obsidian_bots, geode_bots, ore + ore_bots, clay + clay_bots, obsidian + obsidian_bots, geodes + geode_bots, day + 1, blue_print, idle_count + 1)

        return max(obsidian_bot_path, do_nothing_path_1)
        
    do_nothing_path = game(ore_bots, clay_bots, obsidian_bots, geode_bots, ore + ore_bots, clay + clay_bots, obsidian + obsidian_bots, geodes + geode_bots, day + 1, blue_print, idle_count + 1)

    ore_need =  more - ore_bots
    clay_need = blue_print[3][1] - clay_bots

    ore_bot_path = 0
    if (ore >= blue_print[1] and ore_need > 0):
        ore_bot_path = game(ore_bots + 1, clay_bots, obsidian_bots, geode_bots, ore + ore_bots - blue_print[1], clay + clay_bots, obsidian + obsidian_bots, geodes + geode_bots, day + 1, blue_print, 0)

    clay_bot_path = 0
    if (ore >= blue_print[2] and clay_need > 0):
        clay_bot_path = game(ore_bots, clay_bots + 1, obsidian_bots, geode_bots, ore + ore_bots - blue_print[2], clay + clay_bots, obsidian + obsidian_bots, geodes + geode_bots, day + 1, blue_print, 0)


    return max(do_nothing_path, ore_bot_path, clay_bot_path)

max_total = 0

print('running blueprint')
geodes1 = game(1, 0, 0, 0, 0, 0, 0, 0, 1, blue_prints[0], 0)
print('running blueprint')
geodes2 = game(1, 0, 0, 0, 0, 0, 0, 0, 1, blue_prints[1], 0)
print('running blueprint')
geodes3 = game(1, 0, 0, 0, 0, 0, 0, 0, 1, blue_prints[2], 0)

max_total = geodes1 * geodes2 * geodes3

print(max_total)

#print(geodes1)
#print(geodes2)