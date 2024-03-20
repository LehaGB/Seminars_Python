"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

"""
from typing import List
import time

start = time.time()


def function(list_1: List[int], list_2: List[int]) -> List[int]:
    """На входе два списка целых положительных чисел,
    найти все элементы, разнитцу

    Args:
        list_1 (List[int]): целые положительные числа
        list_2 (List[int]): целые положительные числа

    Returns:
        List[int]: разница
    """
    set_list2 = set(list_2)
    return [i for i in list_1 if i not in set_list2]


list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]


if __name__ == '__main__':
    print(*function(list_1, list_2))
    finish = time.time()
    res = finish - start
    res_msec = res * 1000
    print(f'{res_msec}')
