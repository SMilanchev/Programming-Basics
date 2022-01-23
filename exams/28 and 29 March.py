trunk_space = float(input())
total_space_baggage = 0
counter_suitcases = 0
counter = 0


space_volume = input()
while space_volume != 'End':
    counter = counter + 1
    space_to_int = float(space_volume)
    if counter % 3 == 0:
        space_to_int = space_to_int * 1.1

    total_space_baggage = total_space_baggage + space_to_int

    if total_space_baggage > trunk_space:
        print('No more space!')
        break
    else:
        counter_suitcases = counter_suitcases + 1

    space_volume = input()

if trunk_space >= total_space_baggage:
    print('Congratulations! All suitcases are loaded!')

print(f'Statistic: {counter_suitcases} suitcases loaded.')
