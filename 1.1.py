# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input('введите трёхзначное число '))
a = num // 100
b = num // 10 % 10
c = num % 10
print(f'Произведение цифр вашего числа ={a*b*c} /n Сумма цифр вашего числа = {a+b+c}')
print(a, b, c)

