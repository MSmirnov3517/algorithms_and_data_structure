# Определить, является ли год, который ввел пользователь, високосным или не високосным.

y = int(input(' Введите год - '))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 != 0:
            print('обычный год')
        else:
            print('високосный год')
    else:
        print('високосный год')
else:
    print('обычный год')

