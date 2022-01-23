starting_hour = int(input())
starting_mins = int(input())
coming_hour = int(input())
coming_mins = int(input())
mins_to_hours = 0
mins_left = 0
early_or_late = ''

total_mins_of_coming = 60 * coming_hour + coming_mins
total_mins_of_starting = 60 * starting_hour + starting_mins

difference = total_mins_of_coming - total_mins_of_starting

if -30 <= difference <= 0:
    early_or_late = 'On time'
elif difference < -30:
    early_or_late = 'Early'
elif difference > 0:
    early_or_late = 'Late'

if - 60 < difference <= 0 or 60 > difference > 0:
    if difference > 0:
        print(early_or_late)
        print(f'{difference} minutes after the start')
    elif difference <= 0:
        print(early_or_late)
        difference = abs(difference)
        print(f'{difference} minutes before the start')
elif difference <= -60 or difference >= 60:
    if difference <= - 60:
        print(early_or_late)
        difference = abs(difference)
        mins_to_hours = difference // 60
        mins_left = mins_to_hours % 60
        if 1 <= mins_to_hours % 60 <= 9:
            print(f'{mins_to_hours}:0{mins_left} hours before the start')
        else:
            print(f'{mins_to_hours}:{mins_left} hours before the start')
    else:
        print(early_or_late)
        mins_to_hours = difference // 60
        mins_left = mins_to_hours % 60
        if 1 <= mins_to_hours % 60 <= 9:
            print(f'{mins_to_hours}:0{mins_left} hours after the start')
        else:
            print(f'{mins_to_hours}:{mins_left} hours after the start')
