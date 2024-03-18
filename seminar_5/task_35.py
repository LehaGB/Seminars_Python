"""
Задача №35. Общее обсуждение
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes.

"""


def sqrt_number(n: int) -> bool:
    """Находим простое число

    Args:
        n (int): число

    Returns:
        bool: True, False
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True


def prime_number(n: int) -> bool:
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(prime_number(7))
