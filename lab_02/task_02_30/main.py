
# Задание task_02_30.
'''
Дан список целых чисел, введенных с клавиатуры (длина неизвестна). Ответьте на
вопросы:
- являются ли все элементы положительными числами?
- есть ли хотя бы один нулевой элемент в списке?
- являются ли все элементы четными числами?
- есть ли хотя бы один нечетный элемент в списке?
Каждый из пунктов выполните дважды: используя стандартный проход в цикле
(например, через алгоритм с флажком), и используя
функции any() и/или all().
'''
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251



# Все разделенные пробелом элементы будут преобразованы в список целых чисел
nums = [int(item) for item in input().split()]

# 1. Все положительные
for item in nums:
    if item <= 0:
        all_pos_1 = False
        break
else:
    all_pos_1 = True

all_pos_2 = all([item > 0 for item in nums])

# 2. Хотя бы 1 нулевой элемент
for item in nums:
    if item == 0:
        any_zero_1 = True
        break
else:
    any_zero_1 = False

any_zero_2 = any([item == 0 for item in nums])

# 3. Все четные
for item in nums:
    if item % 2 != 0:
        all_even_1 = False
        break
else:
    all_even_1 = True

all_even_2 = all ([item % 2 == 0 for item in nums])

# 4. Хотя бы 1 нечетный элемент
for item in nums:
    if item % 2 != 0:
        any_odd_1 = True
        break
else:
    any_odd_1 = False

any_odd_2 = any ([item % 2 != 0 for item in nums])

print("Все положительные:", all_pos_1, all_pos_2)
print("Хотя бы 1 нулевой элемент:", any_zero_1, any_zero_2)
print("Все четные:", all_even_1, all_even_2)
print("Хотя бы 1 нечетный элемент:", any_odd_1, any_odd_2)

# --------------
# Пример вывода:
#
# -1 1 100 0
# Все положительные: False False
# Хотя бы 1 нулевой элемент: True True
# Все четные: False False
# Хотя бы 1 нечетный элемент: True True
