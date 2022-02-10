profit = int(input('Введите сумму прибыли за месяц '))
debt = int(input('Введите сумму расходов за месяц '))
guys = int(input('Введите количество сотрудников '))
if profit - debt > 0:
    person = profit/guys
    print(f'Ваша фирма отработала в прибыль.Сумма общей прибылиp{profit} Сумма прибыли на человека',person)
elif profit - debt == 0:
    print('Фирма проработала в ноль')
else:
    print('Фирма обанкротилась')