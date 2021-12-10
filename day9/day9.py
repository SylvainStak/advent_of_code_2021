with open('input.txt') as file:
    input = [list(map(lambda x: int(x), line.rstrip())) for line in file.readlines()]

height = len(input)
width = len(input[0])
risk_level = 0

for row in range(len(input)):
    for column in range(len(input[0])):        
        current_location = input[row][column]
        adjacent_locations = []

        if row-1 >= 0:
            adjacent_locations.append(input[row-1][column])
        if row+1 <= height-1:
            adjacent_locations.append(input[row+1][column])
        if column-1 >= 0:
            adjacent_locations.append(input[row][column-1])
        if column+1 <= width-1:
            adjacent_locations.append(input[row][column+1])
        
        is_low = all([False for location in adjacent_locations if location < current_location])
        risk_level += current_location+1 if is_low and current_location != 9 else 0     

print(risk_level)
