"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего
"""
from collections import namedtuple

company = namedtuple('Company', ['name_company', 'profit', 'years_profit'])
all_company = set()
all_profit = 0
avg_profit = 0
num_of_company = int(input('Сколько предприятий у вас есть? - '))
for i in range(num_of_company):
    name_company = input('Введите название компании -')
    profit = []
    years_profit = 0
    for i in range(4):
        profit.append(int(input(f'прибыль за {i} квартал - ')))
        years_profit += profit[i]
    companies = company(name_company=name_company, profit=tuple(profit), years_profit=years_profit)
    all_profit += years_profit
    all_company.add(companies)
avg_profit = all_profit / num_of_company
print(" Компании с прибылью ниже среднего: ")
for companies in all_company:
    if companies.years_profit < avg_profit:
        print(f'Прибыль {companies.name_company} = {companies.years_profit}')

print(" Компании с прибылью выше среднего: ")
for companies in all_company:
    if companies.years_profit >= avg_profit:
        print(f'прибыль {companies.name_company} = {companies.years_profit}')
