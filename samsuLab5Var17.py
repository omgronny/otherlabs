import math

#task 1

a = 3.8

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = float(input("Введите шаг")) 
x = x1

while x <= xn:
  
  y = (1 - math.exp(-a*x))*math.log((a*x**2 - 1)/a*x**2 + 2)
  print("при х = ", x, " y = ", y) 
  x=x+dx


#task 2

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = int(input("Введите шаг")) 

for i in range(x1, xn, dx):  
  y = (1 - math.exp(-a*x))*math.log((a*x**2 - 1)/a*x**2 + 2)
  print("при х = ", i, " y = ", y)


#task 3

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) # вводим по очереди значения с клавиатуры

while (math.sin((n+1)*x))/(2*n+1) > e: # проверяем условие на эпсилон 
  f += (math.sin((n+1)*x))/(2*n+1) # увеличиваем ряд на конкретное значение на данном этапе 
  n+=1 # сдвигаем n по циклу дальше
print('S = ', (f)*0.5) # выводим итоговое значение 

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) # вводим по очереди значения с клавиатуры

while (math.sin((n+1)*x))/(2*n+1) > e: # проверяем условие на эпсилон 
  f += (math.sin((n+1)*x))/(2*n+1) # увеличиваем ряд на конкретное значение на данном этапе 
  n+=1 # сдвигаем n по циклу дальше
print('S = ', (f//1)*0.5) # выводим итоговое значение 


n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) 

while (math.sin((n+1)*x))/(2*n+1) > e: 
  f += (math.sin((n+1)*x))/(2*n+1) 
  n+=1 
print('S = ', (f)*0.5) 
