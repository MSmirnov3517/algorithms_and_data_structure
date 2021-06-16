"""Определить, какое число в массиве встречается чаще всего."""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
b = 0
common = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for i in range(SIZE):
    a = 0
    for y in range(SIZE):
        if array[i] == array[y]:
            a += 1
    if a > b:
        b = a
        common = array[i]
if b == 1:
    print('нет повторяющихся чисел')
else:
    print(f'самое частое число в массиве - {common}')

