whiskey_price = float(input())
beer_quantity = float(input())
wine_quantity = float(input())
rakia_quantity = float(input())
whiskey_quantity = float(input())

total_whiskey = whiskey_price * whiskey_quantity
rakia_price = whiskey_price * 0.5
total_rakia = rakia_quantity * rakia_price
total_beer = beer_quantity * (rakia_price * 0.2)
total_wine = wine_quantity * (rakia_price * 0.6)

total_price = total_beer + total_rakia + total_whiskey + total_wine
print(f'{total_price:.2f}')