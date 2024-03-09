"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9

"""
from random import randrange


number_watermelons = int(input('Введите количество арбузов на прилавке: '))
max_watermelon = 0
min_watermelon = 30001

for i in range(number_watermelons):
    weight_watermelon = randrange(1, 20)
    print(weight_watermelon, end=" ")
    if weight_watermelon > max_watermelon:
        max_watermelon = weight_watermelon
        
    if min_watermelon > weight_watermelon:
        min_watermelon = weight_watermelon
print()
print(f'{max_watermelon} кг максимальный вес арбуза')
print(f'{min_watermelon} кг минимальный вес арбуза')
       
