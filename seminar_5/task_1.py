
"""
 Объявление функций, аргументы, возвращаемое значение, анатации
"""

def sum_func(a: int, b: int) -> int:
    """returns the amount a and b 

    Args:
        a (int): number
        b (int): number

    Returns:
        int: the sum of the number
    """    
    return a + b
print(sum_func(2, 5))