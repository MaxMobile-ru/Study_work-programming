# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_02_22.
#
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251
# E-mail: stavetskiimi099@mgpu.ru


n = int (input ('n = '))

a_max = None
a_min = None

for i in range (1, n + 1):
    num = float (input (f'{i}-е число = '))
    if a_max == None and a_min == None:
        a_max = num
        a_min = num
        continue
    a_max = max (a_max, num)
    a_min = min (a_min, num)

print("Максимум: {:.2f}".format(a_max))
print("Минимум: {:.2f}".format(a_min))

# --------------
# Пример вывода:
#
# n = 4
# 1-е число = 6.2
# 2-е число = 3.8
# 3-е число = 1.1
# 4-е число = 9.66
# Максимум: 9.66
# Минимум: 1.10
