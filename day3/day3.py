with open('input.txt') as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

def find_commons(list):
    counter_list = [{'0': 0, '1': 0} for i in range(len(list[0]))]

    for binary in list:
        for index in range(len(binary)):
            if binary[index] == '0':
                counter_list[index]['0'] += 1
            else:
                counter_list[index]['1'] += 1
    
    return counter_list

# Part 1
gammarate = []
epsilonrate = []

counter_list = find_commons(input)

for counter in counter_list:
    if counter['0'] > counter['1']:
        gammarate.append('0')
        epsilonrate.append('1')
    else:
        gammarate.append('1')
        epsilonrate.append('0')

gammarate = int(''.join(gammarate), 2)
epsilonrate = int(''.join(epsilonrate), 2)
power_consumption = gammarate*epsilonrate

print(power_consumption)

# Part 2
oxygen_rating = input
CO2_rating = input
considered_bit = 0

while len(oxygen_rating) > 1:
    temp = oxygen_rating
    oxygen_rating = []
    commons = find_commons(temp)
    most_common = ''
    if commons[considered_bit]['0'] > commons[considered_bit]['1']:
        most_common = '0'
    elif  commons[considered_bit]['0'] < commons[considered_bit]['1']:
        most_common = '1'
    else:
        most_common = '1'

    for binary in temp:
        if binary[considered_bit] == most_common:
            oxygen_rating.append(binary)
    
    considered_bit += 1

considered_bit = 0
    
while len(CO2_rating) > 1:
    temp = CO2_rating
    CO2_rating = []
    commons = find_commons(temp)
    least_common = ''
    if commons[considered_bit]['0'] > commons[considered_bit]['1']:
        least_common = '1'
    elif  commons[considered_bit]['0'] < commons[considered_bit]['1']:
        least_common = '0'
    else:
        least_common = '0'

    for binary in temp:
        if binary[considered_bit] == least_common:
            CO2_rating.append(binary)
    
    considered_bit += 1

oxygen_rating_score = int(''.join(oxygen_rating), 2)
CO2_rating_score = int(''.join(CO2_rating), 2)
life_support_rating = oxygen_rating_score*CO2_rating_score

print(life_support_rating)
