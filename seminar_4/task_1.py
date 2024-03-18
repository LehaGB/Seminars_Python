"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()

"""
s = 'aaabcaadcdd'
dict_n = {}
count = 0
res = ''
for i in s:
    if i not in dict_n:
        dict_n[i] = 0
        res += i
    else:
        dict_n[i] += 1
        res += f'{i}_{dict_n[i]}'

print(res)
        

