
# Задание task_02_34.
#
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251



# 1. Заполнение списка

# Используйте данный список для собственных тестов,
# чтобы избежать постоянного ввода значений
# Перед автоматической проверкой удалите его
# и используйте ввод с клавиатуры
#deposits = [
#    {"name": "Банк_1", "initial_sum": 50000, "rate": 5.2},
#    {"name": "Банк_2", "initial_sum": 20000, "rate": 3.7},
#    {"name": "Банк_3", "initial_sum": 45000, "rate": 6.8},
# ]

n = int (input ('Количество банков = '))

deposits = []
for _ in range (n):
    lst = input ().split ()
    deposits.append ({'name': lst [0], 'initial_sum': int (lst [1]), 'rate': float (lst [2])})

# 2. Самый доступный банк (с наименьшей первоначальной суммой)
min_init_sum = deposits [0] ['initial_sum']
min_init_sum_name = deposits [0] ['name']
for item in deposits:
    if item ['initial_sum'] < min_init_sum:
        min_init_sum = item ['initial_sum']
        min_init_sum_name = item ['name']
print ('Самый доступный банк: {}, первоначальная сумма: {:.2f} руб.'.format (min_init_sum_name, float (min_init_sum)))

# 3. Самый выгодный банк
#    прибыль = сумма * процент / 100

pribyl = deposits [0] ['initial_sum'] * deposits [0] ['rate'] / 100
pribyl_name = deposits [0] ['name']
for item in deposits:
    if item ['initial_sum'] * item ['rate'] / 100 > pribyl:
        pribyl = item ['initial_sum'] * item ['rate'] / 100
        pribyl_name = item ['name']
print ('Самый выгодный банк: {}, прибыль: {:.2f} руб.'.format (pribyl_name, pribyl))

# --------------
# Пример вывода:
#
# Количество банков = 3
# Банк_1 50000 5.2
# Банк_2 20000 3.7
# Банк_3 45000 6.8
# Самый доступный банк: Банк_2, первоначальная сумма: 20000.00 руб.
# Самый выгодный банк: Банк_3, прибыль: 3060.00 руб.
