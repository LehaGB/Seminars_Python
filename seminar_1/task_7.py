"""
Задача № 7

Дано натуральное число.
Требуется определить, является ли год с данным номером високосным.
Если год является вискосным, то вывидите YES, иначе вывидите NO.
Напомним, что в соответствии с григорианским календарем, год
является високосным, если его номер кратен 4, но нре кратен 100,
а также если он кратен 400.
"""

#i = int(input('Введите год: '))
for i in range(1950, 2001):
    if (i % 4 == 0) and (i % 100 != 0 or i % 400 == 0):
        print(f'YES =  {i} - високосный год')
    else:
        print('NO')