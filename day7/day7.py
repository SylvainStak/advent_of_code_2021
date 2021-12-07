import sys

with open('input.txt') as file:
    input = file.readline().split(',')
    input = list(map(lambda x: int(x), input))

# Part 1
min_fuel_position = sys.maxsize

for position in range(max(input)):
    total_fuel = sum([abs(i-position) for i in input])
    min_fuel_position = total_fuel if total_fuel < min_fuel_position else min_fuel_position

print(min_fuel_position)

# Part 2
min_fuel_position = sys.maxsize

for position in range(max(input)):
    total_fuel = sum([sum(range(abs(i-position) + 1)) for i in input])
    min_fuel_position = total_fuel if total_fuel < min_fuel_position else min_fuel_position

print(min_fuel_position)