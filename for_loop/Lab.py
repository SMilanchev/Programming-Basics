days = int(input())
room_type = input()
grade = input()

nights = days-1
price_nights = 0
discounted_price_nights = 0

if room_type == 'room for one person':
    discounted_price_nights = 18 * nights
elif room_type == 'apartment':
    price_nights = 25 * nights
    if nights < 10:
        discounted_price_nights = price_nights * 0.7
    elif 10 <= nights <= 15:
        discounted_price_nights = price_nights * 0.65
    else:
        discounted_price_nights = price_nights * 0.5
elif room_type == 'president apartment':
    price_nights = 35 * nights
    if nights < 10:
        discounted_price_nights = price_nights * 0.9
    elif 10 <= nights <= 15:
        discounted_price_nights = price_nights * 0.85
    else:
        discounted_price_nights = price_nights * 0.8

if grade == 'positive':
    discounted_price_nights = discounted_price_nights * 1.25
else:
    discounted_price_nights = discounted_price_nights * 0.9

print(f'{discounted_price_nights:.2f}')
