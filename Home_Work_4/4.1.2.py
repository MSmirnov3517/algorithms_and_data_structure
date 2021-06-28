"""Определить, какое число в массиве встречается чаще всего."""

import random
import timeit
import cProfile

def frequently(size):

    MIN_ITEM = 0
    MAX_ITEM = 100

    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    return num

number = 100
while number < 2000:
    number += 100
    t_it = timeit.timeit('frequently(number)', number=100, globals=globals())
    print(f'{number=:<4}  {t_it=:>10.7f}')

cProfile.run('frequently(number)')

"""
number=200   t_it= 0.0181673
number=300   t_it= 0.0271474
number=400   t_it= 0.0359484
number=500   t_it= 0.0448283
number=600   t_it= 0.0540986
number=700   t_it= 0.0626186
number=800   t_it= 0.0720893
number=900   t_it= 0.0804840
number=1000  t_it= 0.0915447
number=1100  t_it= 0.1039149
number=1200  t_it= 0.1158488
number=1300  t_it= 0.1133791
number=1400  t_it= 0.1396078
number=1500  t_it= 0.1305967
number=1600  t_it= 0.1558648
number=1700  t_it= 0.1532762
number=1800  t_it= 0.1613879
number=1900  t_it= 0.1652185
number=2000  t_it= 0.1996062
         10541 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.004    0.004 4.1.2.py:12(<listcomp>)
        1    0.000    0.000    0.004    0.004 4.1.2.py:7(frequently)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
     2000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     2000    0.001    0.000    0.003    0.000 random.py:290(randrange)
     2000    0.001    0.000    0.003    0.000 random.py:334(randint)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2536    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""