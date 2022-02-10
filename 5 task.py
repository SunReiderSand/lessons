profit = int(input('Введите сумму прибыли за месяц'))
debt = int(input('Введите сумму расходов за месяц'))
if profit/debt > 0:
    print('Ваша фирма отработала в прибыль')
elif profit/debt == 0:
    print('Фирма проработала в ноль')
else:
    print('Фирма обанкротилась')