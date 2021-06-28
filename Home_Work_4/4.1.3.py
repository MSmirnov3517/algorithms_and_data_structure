"""Определить, какое число в массиве встречается чаще всего."""

import random
import timeit
import cProfile


def frequently(size):
    MIN_ITEM = 0
    MAX_ITEM = 100

    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

    return max(array, key=array.count)


number = 100
while number < 2000:
    number += 100
    t_it = timeit.timeit('frequently(number)', number=100, globals=globals())
    print(f'{number=:<4}  {t_it=:>10.7f}')

cProfile.run('frequently(number)')

"""
number=200   t_it= 0.0796891
number=300   t_it= 0.1415860
number=400   t_it= 0.2200697
number=500   t_it= 0.3287155
number=600   t_it= 0.4534073
number=700   t_it= 0.6050955
number=800   t_it= 0.8264418
number=900   t_it= 1.0377204
number=1000  t_it= 1.2050871
number=1100  t_it= 1.4819738
number=1200  t_it= 1.7969852
number=1300  t_it= 2.0576388
number=1400  t_it= 2.5182572
number=1500  t_it= 2.6916879
number=1600  t_it= 3.1658489
number=1700  t_it= 3.4774322
number=1800  t_it= 3.8595579
number=1900  t_it= 4.3077367
number=2000  t_it= 4.7928742
         10495 function calls in 0.049 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.004    0.004 4.1.3.py:12(<listcomp>)
        1    0.000    0.000    0.049    0.049 4.1.3.py:8(frequently)
        1    0.000    0.000    0.049    0.049 <string>:1(<module>)
     2000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
     2000    0.001    0.000    0.002    0.000 random.py:290(randrange)
     2000    0.001    0.000    0.003    0.000 random.py:334(randint)
        1    0.000    0.000    0.049    0.049 {built-in method builtins.exec}
        1    0.045    0.045    0.045    0.045 {built-in method builtins.max}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2489    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


"""

"""
Вот это стало для меня неожиданным. Решение в одну строчку работает дольше, чем решение 4.1.2 со списком.
Насколько я понял функция max медленно обрабатывает данные..
"""