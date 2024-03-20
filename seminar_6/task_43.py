"""
Задача №43.
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:                               Вывод:
1 2 3 2 3                             2
"""

from typing import List


def pairs_of_numbers(array: List[int]) -> int:
    count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
    return count


array = [1, 2, 3, 2, 3]


def couple(arr: List[int]) -> int:
    return len(arr) - len(set(arr))


arr1 = [1, 2, 3, 2, 3, 5, 4, 5, 4, 5]

if __name__ == '__main__':
    print(couple(arr1))
