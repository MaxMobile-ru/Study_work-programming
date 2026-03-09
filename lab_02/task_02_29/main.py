
# Задание task_02_29.
#
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251



n = int(input("n = "))

nums = [float (input (f'Введите {i}-й элемент списка: ')) for i in range (1, n + 1)]

nums_pos = [x for x in nums if x > 0]
nums_neg = list ()
for i in nums:
    if i < 0:
        nums_neg.append (i)

sr_ar = sum (nums_pos) / len (nums_pos)
sr_geom = 1
for i in nums_neg:
    sr_geom *= i
sr_geom = sr_geom ** (1/len (nums_neg))

print ('Исходный список:', nums)
print ('Положительные числа:', nums_pos)
print ('Отрицательные числа:', nums_neg)
print ('Ср. арифм.: {:.2f}'.format (sr_ar))
print ('Ср. геом.: {:.2f}'. format (sr_geom))

# --------------
# Пример вывода:
#
# n = 4
# Введите 1-й элемент списка: 1
# Введите 2-й элемент списка: 6
# Введите 3-й элемент списка: -10
# Введите 4-й элемент списка: -3
# Исходный список: [1.0, 6.0, -10.0, -3.0]
# Положительные числа: [1.0, 6.0]
# Отрицательные числа: [-10.0, -3.0]
# Ср. арифм.: 3.50
# Ср. геом.: 5.48
