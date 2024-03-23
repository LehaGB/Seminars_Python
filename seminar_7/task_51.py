"""
Задача №51.
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:                                    Вывод:
values = [0, 2, 10, 6]                    same
if same_by(lambda x: x % 2, values):
print('same')
else:
print('different')

"""


def same_by(charc, obj) -> int:
    obj = (map(charc, obj))
    return all(obj) or not any(obj)


element1 = [2, 4, 6, 8, 10]
element2 = [1, 2, 3, 4, 5]
element3 = [1, 3, 5, 7, 9]

if __name__ == '__main__':
    print(element1, same_by(lambda x: x % 2 == 0, element1))
    print(element2, same_by(lambda x: x % 2 == 0, element2))
    print(element3, same_by(lambda x: x % 2 == 0, element3))


# def same_by(element: list) -> bool:
#     flag = True
#     for i in range(len(element)):
#         flag = flag and (return_bbol(element[i])) or (return_bbol(element[i]))
#     return flag


# def return_bbol(element: int) -> bool:
#     return element % 2 == 0 or not element % 3 != 0


# element1 = [2, 4, 6, 8, 10]
# element2 = [1, 2, 3, 4, 5]
# element3 = [1, 3, 5, 7, 9]
# element4 = []


# if __name__ == '__main__':
#     print(element1, same_by(element1))
#     print(element2, same_by(element2))
#     print(element3, same_by(element3))
#     print(element4, same_by(element4))
