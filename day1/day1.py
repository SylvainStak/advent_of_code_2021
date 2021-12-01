with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
last = int(lines[0])
increased = 0

for measurement in lines:
    if int(measurement) > last:
        increased += 1
    last = int(measurement)

print(increased)

# Part 2
last_sum = int(lines[0])+int(lines[1])+int(lines[2])
increased = 0

for index in range(len(lines)-2):
    sum = int(lines[index])+int(lines[index+1])+int(lines[index+2])
    if sum > last_sum:
        increased += 1
    last_sum = sum

print(increased)
