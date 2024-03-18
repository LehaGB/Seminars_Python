"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

"""
from copy import copy
from typing import List
def max_min_number(nums: List[int]) -> List[int]:
    """Возвращает список 

    Args:
        nums (List[int]): список чисел.

    Returns:
        List[int]: новый заменённый список(максимальные – на минимальные.)
    """
    min_n = min(nums)
    max_n = max(nums)
    new_marks = copy(nums)
    for i in range(len(new_marks)):
        if new_marks[i] == max_n:
            new_marks[i] = min_n
    return new_marks

marks = [1, 3, 4, 1, 5, 1, 5]
print(marks)

   
if __name__== '__main__':
   print(max_min_number(marks))
    
            


