
# Задание task_02_10.
#
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251
# E-mail: stavetskiimi099@mgpu.ru


n = int (input ('n = '))

n_sum = 0
n_count = 0

while n != 0:
    n_count += 1
    num = n % 10
    n_sum += num
    n = n // 10

print ('Сумма =', n_sum)
print ('Количество =', n_count)

# --------------
# Пример вывода:
#
# n = 12345
# Сумма = 15
# Количество = 5
