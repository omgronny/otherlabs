""" Задание №1. Применение операторов цикла к работе со строкам
Запросить у пользователя случайную букву и заменить все
буквы строки, стоящие на четных позициях на данную букву. """


string = input('Введите строку: ')                      # ввод строки
b = input('Введите букву: ')                            # ввод буквы
stringArray = list(string)                              # формируем список из символов строки
for i in range(0, len(stringArray) - 1, 2):             # проходимся в цикле по четным элементам массива и заменяем их на букву b
    if stringArray[i] != ' ':
        stringArray[i] = b                              # производим замену

string = "".join(stringArray)                           # с помощью join формируем строку из списка символов

print('Полученная строка: \n' + string)                 # выводим результат




""" Задание № 2. Применение операторов цикла к работе со списками
Список из N элементов. В заданном списке поменять местами соседние 
элементы, стоящие на чётных местах, с элементами, стоящими на нечётных. """

n = int(input('Введите количество элементов списка: ')) # ввод кол-ва элементов списка
N = [0] * n                                             # объявление списка на n элементов
print('Введите элементы списка по одному в строке: ')
for i in range(n):                                      # заполнение списка
    N[i] = int(input())

for i in range(1, n, 2):                                # проходимся по всем элементам списка на нечетных местах
    N[i], N[i - 1] = N[i - 1], N[i]                     # и меняем их местами с элементами, стоящими на четных местах

print('Полученный список:\n', N)                        # выводим результат