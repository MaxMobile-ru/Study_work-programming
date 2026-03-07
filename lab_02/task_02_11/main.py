
# Задание task_02_11.
#
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251



start = int (input ('start = '))
k = int (input ('k = '))
s = int (input ('s = '))
n_count = 0

while n_count <= 10:
    if start % 10 == k and start % s == 0:
        print (start, end=' ')
        n_count += 1
    start += 1

# --------------
# Пример вывода:
#
# start = 100
# k = 7
# s = 9
# 117 207 297 387 477 567 657 747 837 927
