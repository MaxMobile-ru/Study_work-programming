
# Задание task_03_01_07.
# Вариант 24
'''
Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру.
'''
# Выполнил: Ставецкий Максим Иванович
# Группа: ЦИБ-251



def has_digits(sentence):
    """Определяет наличие цифр.
    
    Параметры:
        sentence (str): текст предложения.
    Результат:
        bool: True - да, False - нет."""
    example = '0123456789'
    for item in example:
        if item in sentence:
            return True
    return False


def sentences_with_digits_count(sentences):
    """Вычисляет количество предложений с цифрой.
    
    Параметры:
        sentences (str): текст предложений.
    Результат:
        counter (int): искомое количество предложений."""
    lst1 = sentences.split ('|')
    counter = 0
    for item in lst1:
        if has_digits (item):
            counter += 1
    return counter


n = int (input ('Введите количество предложений: '))
text = ''

for i in range (1, n + 1):
    entire = input (f'Введите предложение №{i}:\n')
    text += entire + '|'

print ('Предложений с цифрой =', sentences_with_digits_count (text))

# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1
