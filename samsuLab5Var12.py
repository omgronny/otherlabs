
import math

#task 1

a = 1.9
b = 1.1

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = float(input("Введите шаг"))   # Вводим значения
x = x1

while x <= xn: # Пока х меньше или равен xn
  
  y = a*math.log(x/(b*x**2 + 2)) 
  print("при х = ", x, " y = ", y) # Печатаем формулу
  x=x+dx # и увеличиваем икс


#task 2

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = int(input("Введите шаг"))  # Вводим значения 

for i in range(x1, xn, dx):  # цикл от начала до конца с шагом дельта икс 
  y = a*math.log(x/(b*x**2 + 2)) 
  print("при х = ", i, " y = ", y) # Выводим значение выражения


#task 3

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) 
while (x**n)/n > e: 
  f += (x**n)/n   
  n+=1 
print('S = ', f + 1)  

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) # вводим по очереди значения с клавиатуры

while (x**n)/n > e: # проверяем условие на эпсилон 
  f += (x**n)/n  # увеличиваем ряд на конкретное значение на данном этапе 
  n+=1 # сдвигаем n по циклу дальше
print('S = ', f + 1) # выводим итоговое значение 


n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) # вводим по очереди значения с клавиатуры

while (x**n)/n > e: # проверяем условие на эпсилон 
  f += (x**n)/n  # увеличиваем ряд на конкретное значение на данном этапе 
  n+=1 # сдвигаем n по циклу дальше
print('S = ', f + 1) # выводим итоговое значение 
