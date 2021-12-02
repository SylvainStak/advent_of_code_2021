with open('input.txt') as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

# Part 1
horizontal = 0
depth = 0

for x in input:
    splitted = x.split(' ')
    direction = splitted[0]
    distance = int(splitted[1])

    if direction == 'forward':
        horizontal += distance

    if direction == 'up':
        depth -= distance

    if direction == 'down':
        depth += distance

print(horizontal*depth)

# Part 2
horizontal = 0
depth = 0
aim = 0

for x in input:
    splitted = x.split(' ')
    direction = splitted[0]
    distance = int(splitted[1])

    if direction == 'forward':
        horizontal += distance
        depth += aim*distance

    if direction == 'up':
        aim -= distance

    if direction == 'down':
        aim += distance

print(horizontal*depth)
