"""
Повторение.
Генераторные выражения.
"""
numbers_list = [i for i in range(1, 11)]
print(numbers_list)

# Выводится одна буква f , так как множества содержат только уникальные элементы.
numbers_set = {"f" for i in range(1, 11)}
print(numbers_set)

numbers_dict = {i: "f" for i in range(1, 11)}
print(numbers_dict)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

even_numbers_or_0 = [i if i % 2 == 0 else i**2 for i in range(1, 11)]
print(even_numbers_or_0)

# В этом случае первое действие происходит for j in range(10, 20), а потом for i in range(1,10)
number = [i*j for i in range(1,10) for j in range(10, 20)]
print(number)