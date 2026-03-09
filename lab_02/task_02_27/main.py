
# Задание task_02_27.
#
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251



n = int (input ('n = '))
count = 0
i = 2


while count < n:
    count_del = 0
    for j in range (1, i + 1):
        if i % j == 0:
            count_del += 1
    if count_del == 2:
        print (i, end=' ')
        count += 1
    i += 1

# --------------
# Пример вывода:
#
# n = 10
# 2 3 5 7 11 13 17 19 23 29
