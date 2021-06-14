# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def func(a, odd=0, even=0):
    if a == 0:
        return f'четных - {even}, не четных - {odd}'
    if (a % 10) % 2 != 0:
        return func(a // 10, odd + 1, even)
    return func(a // 10, odd,  even + 1)

z = func(112131315498723106886403870623189670)
print(z)