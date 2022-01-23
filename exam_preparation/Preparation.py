participants = int(input())
name = ''
sweet_type = ''
baked_sweets = 0
stop_baking = False
price = 0
total_cakes = 0
total_cookies = 0
total_waffles = 0

for i in range(participants):
    name = input()
    cookies_counter = 0
    cakes_counter = 0
    waffles_counter = 0
    for r in range(3):
        sweet_type = input()
        if sweet_type == 'Stop baking!':
            stop_baking = True
            break
        baked_sweets = int(input())
        if sweet_type == 'cookies':
            cookies_counter = cookies_counter + baked_sweets
        elif sweet_type == 'cakes':
            cakes_counter = cakes_counter + baked_sweets
        elif sweet_type == 'waffles':
            waffles_counter = waffles_counter + baked_sweets

    total_cakes = total_cakes + cakes_counter
    total_cookies = total_cookies + cookies_counter
    total_waffles = total_waffles + waffles_counter

    print(f'{name} baked {cookies_counter} cookies, {cakes_counter} cakes and {waffles_counter} waffles.')

print(f'All bakery sold: {(total_waffles + total_cookies + total_cakes)}')
total_sum = total_cakes * 7.8 + total_cookies * 1.5 + total_waffles * 2.3
print(f'Total sum for charity: {total_sum:.2f} lv.')