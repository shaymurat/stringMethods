my_string = input('Введите произвольный текст ')

# Вывести количество символов введённого текста
print('Вы ввели', len(my_string), 'символов')

# Выведите строку my_string в верхнем регистре.
print(my_string.upper())

# Выведите строку my_string в нижнем регистре.
print(my_string.lower())

# Измените строку my_string, удалив все пробелы.
print(my_string.replace(' ', ''))
# Если именно ИЗМЕНИТЬ, то
# my_string = my_string.replace(' ', '')

# Выведите первый символ строки my_string.
print(my_string[0])

# Выведите последний символ строки my_string.
print(my_string[-1])
