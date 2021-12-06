with open('input.txt') as file:
    input = file.readline().split(',')
    input = list(map(lambda x: int(x), input))

def countFishes(days):
    for day in range(days):
        new_fishes = []
        for fish in range(len(input)):
            input[fish] -= 1
            if input[fish] == -1:
                input[fish] = 6
                new_fishes.append(8)
        input.extend(new_fishes)
    
    return len(input)

# Part 1
print(countFishes(80))

# Part 2
print(countFishes(256))
