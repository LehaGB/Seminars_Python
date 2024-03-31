"""
Работа с файлами.
"""

# Открытие и чтение файла.
with open("text.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Запись в файл, старое удаляет, а новое записывает.
with open("text.txt", "w", encoding="utf-8") as file:
    file.write("New text" + " ")

# Дозаписывает в файл.Продолжая текст.
with open("text.txt", "a", encoding="utf-8") as file:
    file.write("added string")


with open("text.txt", "r", encoding="utf-8") as file:
    print(file.read())
