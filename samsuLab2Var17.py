

#task 1
a=2.44
b=1.39
c=6.21
x=float(input("Введите значение х ")) # Вводим значение 

y=a*x + (b*x**2 - 1)/(c*x**2 + 3) #  Формула из варианта

print('y = ', y) # Выводим значение


#task 2

n = input("Введите строку ") # Вводим строку

print(len(n))  # Выводим длину строки 

for i in range(5): # Выводим элементы согласно заданию в цикле
  print(n[-3])


#task 3
s1 = list(input()) # вводим первый список
s2 = [1, 2] # задаем второй список
s3 = s1 + s1 # задаем третий список
print(s1)
print(s2)
print(s3) # выводим списки по очереди

for i in range(3,12,2):       # так как массивы нумеруются с нуля, чтобы посчитать с 4й по 12ю строку, мы должны указать с 3 по 12 (не по 11, потому что синтаксис цикла for  
  print(s1[i])                # таков, что последнее значение, которое ты кажешь, он не возьмёт
print(s2[0]/s2[1] - s2[0]//s2[1], end = ' ') # выводим дробную часть числа
