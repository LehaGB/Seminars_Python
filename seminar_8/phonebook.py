"""
Телефонная книга.
"""

import os
import sys


def add_new_aser(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(file, "a", encoding="utf-8") as filename:
        filename.write(f"{new_line}{name}: {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает всё содержимое телефонной книги.
    """
    with open(file, "r", encoding="utf-8") as filename:
        return filename.read()


def read_all_new_file(f2: str) -> str:
    """
    Возвращает всё содержимое нового файла
    """
    with open(new_file, "r", encoding="utf-8") as filename:
        return filename.read()


def search_user(file: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(file, "r", encoding="utf-8") as filename:
        result = []
        list_1 = filename.read().split('\n')
        result = [i for i in list_1 if data in i]
        if not result:
            return "По указанному значению совпадений не найдено"
        return '\n'.join(result)


def transfer_data(source: str, dest: str):
    """
    Перенос записи в другой файл
    """
    name_file1 = input("Введите имя, которое нужно переместить на другой файл: ")
    with open(file, 'r', encoding="utf-8") as source, open(new_file, 'w', encoding="utf-8") as dest:
        text = source.readlines()
        for _line in text:
            if name_file1 in _line:
                for k in _line:
                    dest.write(k)


INFO_STRING = """
Выбирите режим работы:
1 - вывести данные
2 - добавление нового пользователя
3 - поиск
4 - пернести запись в другой файл
5 - вывести данные с нового файла
"""


file = "phonebook.txt"
new_file = "namebook.txt"


if file not in os.listdir():
    print("Указанное имя файла отсутствует")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите своё имя: ")
        phone = input("Введите свой номер телефона: ")
        print(add_new_aser(name=name, phone=phone, filename=file))
    elif mode == 3:
        data = input("Введите номер: ")
        print(search_user(file=file, data=data))
    elif mode == 4:
        print(transfer_data(file, new_file))
    elif mode == 5:
        print(read_all_new_file(new_file))
