salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital_new = 0
for i in range(months):
    if i == 0:
        money = spend - salary
    else:
        spend *= 1 + increase
        money = round(spend - salary)
    money_capital_new += money
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital_new)
