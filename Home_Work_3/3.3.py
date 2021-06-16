"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
max_num = 0
min_num = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for i in range(SIZE):
    b = 0
    c = 0
    for z in range(SIZE):
        if array[i] < array[z]:
            b += 1
        else:
            c += 1
        if b == SIZE - 1:
            min_num = i
        if c == SIZE:
            max_num = i
array[max_num], array[min_num] = f'* {array[min_num]} * ', f'* {array[max_num]} *'   # '*' - что бы видеть заменяемые
# элементы)
print(array)