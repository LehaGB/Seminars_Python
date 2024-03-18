"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию

"""
def numbers_fib(n)->int:
    if n in [1, 2]:
        return 1
    return numbers_fib(n - 1) + numbers_fib(n - 2)

list_fib = []
for i in range(1, 10):
    list_fib.append(numbers_fib(i))
print(list_fib)