n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for nums in range(1, n + 1):
    num = int(input())
    if 1 <= num < 200:
        p1 = p1 + 1
    elif 200 <= num < 400:
        p2 = p2 + 1
    elif 400 <= num < 600:
        p3 = p3 + 1
    elif 600 <= num < 800:
        p4 = p4 + 1
    elif 800 <= num <= 1000:
        p5 = p5 + 1

p1_total = (p1 / n) * 100
p2_total = (p2 / n) * 100
p3_total = (p3 / n) * 100
p4_total = (p4 / n) * 100
p5_total = (p5 / n) * 100

print(f'{p1_total:.2f}%')
print(f'{p2_total:.2f}%')
print(f'{p3_total:.2f}%')
print(f'{p4_total:.2f}%')
print(f'{p5_total:.2f}%')