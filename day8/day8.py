with open('input.txt') as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

accepted_lengths = [2,4,3,7]
counter = 0

for line in input:
    splitted_line = line.split('|')
    output_values = splitted_line[1].strip().split(' ')

    for digit in output_values:
        counter += 1 if len(digit) in accepted_lengths else 0
    
print(counter)
