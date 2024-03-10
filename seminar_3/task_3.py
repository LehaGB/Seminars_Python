"""
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""

from functools import reduce


my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

res = set()
for d in my_dict:
    res = res.union(set(d.values()))
    # for el in d.values():
    #     res.add(el)
print(res)
# print(set(my_dict.values()))


    