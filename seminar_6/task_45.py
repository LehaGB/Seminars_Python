"""
Задача №45.
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:                Вывод:
300                  220 284

"""


def friendly_number(number: int) -> int:
    count = 1
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            count += (i + number//i)
    return count


k = int(input('Ввидите число: '))


def result_sum(k: int) -> dict:
    set_result = dict()
    for i in range(220, k):
        res = friendly_number(i)
        if i == res or i in set_result or res in set_result:
            continue
        if friendly_number(res) == i:
            set_result.update({i: res})
    return set_result


if __name__ == '__main__':
    print(result_sum(k))
