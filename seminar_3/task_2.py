"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.

"""
# list_1 =  [1, 2, 3, 4]
# k = 3

# for i in range(k):
#     n = list_1.pop(len(list_1) -1)
#     list_1.insert(0, n)           
# print(list_1)

# Решение с помощью срезов.
list_2 =  [1, 2, 3, 4]
k = 3
shift = k % len(list_2)
res = list_2[len(list_2)-shift:len(list_2)] +  list_2[0:len(list_2) -shift]
print(res)