import math

#task 1

a = 1.92

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = float(input("Введите шаг")) # Вводим значения 
x = x1

while x <= xn: # Пока х меньше или равен xn
  
  y = ((a**2)*math.sin(x**2))/(a + (math.sin(x))**2)
  print("при х = ", x, " y = ", y) # Печатаем формулу
  x=x+dx # и увеличиваем икс


#task 2

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = int(input("Введите шаг"))   # Вводим значения

for i in range(x1, xn, dx):   # цикл от начала до конца с шагом дельта икс
  y = ((a**2)*math.sin(x**2))/(a + (math.sin(x))**2)
  print("при х = ", i, " y = ", y) # Выводим значение выражения


#task 3

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) # Вводим значения

while math.cos(n*x)/n > e: # Пока значение больше эпсилон
  f += math.cos(n*x)/n # Увеличиваем значение f
  n+=1 # Увеличиваем значение n
print('S = ', f) # Выводим результат

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) 

while math.cos(n*x)/n > e:  
  f += math.cos(n*x)/n  
  n+=1 
print('S = ', (f)) 


n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) 

while math.cos(n*x)/n > e: 
  f += math.cos(n*x)/n
  n+=1 
print('S = ', (f)) 
