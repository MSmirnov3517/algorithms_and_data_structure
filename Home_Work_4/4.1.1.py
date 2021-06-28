"""Определить, какое число в массиве встречается чаще всего."""

import random
import timeit
import cProfile


def frequently(size):
    array = [random.randint(0, 100) for _ in range(size)]

    b = 0
    common = 0
    for i in range(size):
        a = 0
        for y in range(size):
            if array[y] == array[i]:
                a += 1
            if a > b:
                b = a
                common = array[i]
    return common


number = 100
while number < 2000:
    number += 100
    t_it = timeit.timeit('frequently(number)', number=100, globals=globals())
    print(f'{number=:<4}  {t_it=:>10.7f}')

cProfile.run('frequently(number)')

"""
 number=200   t_it= 0.0881508
number=300   t_it= 0.1847229
number=400   t_it= 0.3024118
number=500   t_it= 0.3833550
number=600   t_it= 0.5880175
number=700   t_it= 0.6928086
number=800   t_it= 0.9271472
number=900   t_it= 1.1107605
number=1000  t_it= 1.3015094
number=1100  t_it= 1.5176306
number=1200  t_it= 1.8621900
number=1300  t_it= 2.9797821
number=1400  t_it= 2.5012038
number=1500  t_it= 2.9556282
number=1600  t_it= 3.3111765
number=1700  t_it= 4.7099470
number=1800  t_it= 4.0957447
number=1900  t_it= 5.1375082
number=2000  t_it= 5.3694418
         10548 function calls in 0.058 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.004    0.004 3.4.2.py:12(<listcomp>)
        1    0.000    0.000    0.058    0.058 3.4.2.py:8(frequently)
        1    0.000    0.000    0.058    0.058 <string>:1(<module>)
     2000    0.001    0.000    0.002    0.000 random.py:237(_randbelow_with_getrandbits)
     2000    0.001    0.000    0.003    0.000 random.py:290(randrange)
     2000    0.001    0.000    0.004    0.000 random.py:334(randint)
        1    0.000    0.000    0.058    0.058 {built-in method builtins.exec}
        1    0.053    0.053    0.053    0.053 {built-in method builtins.max}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2542    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""