import sys

n = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize

for num in range(1, n + 1):
    number = float(input())
    if num % 2 == 1:
        odd_sum = odd_sum + number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    else:
        even_sum = even_sum + number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
if (even_min == sys.maxsize and even_max == - sys.maxsize) and (odd_min == sys.maxsize and odd_max == - sys.maxsize):
    print(f'OddSum={odd_sum:.2f},')
    print('OddMin=No,')
    print('OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif odd_min == sys.maxsize and odd_max == - sys.maxsize:
    print(f'OddSum={odd_sum:.2f},')
    print('OddMin=No,')
    print('OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
elif even_min == sys.maxsize and even_max == - sys.maxsize:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')