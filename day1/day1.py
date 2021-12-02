with open('input.txt') as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

# Part 1
last = int(input[0])
increased = 0

for measurement in input:
    if int(measurement) > last:
        increased += 1
    last = int(measurement)

print(increased)

# Part 2
last_sum = int(input[0])+int(input[1])+int(input[2])
increased = 0

for index in range(len(input)-2):
    sum = int(input[index])+int(input[index+1])+int(input[index+2])
    if sum > last_sum:
        increased += 1
    last_sum = sum

print(increased)
