import math

#task 1

a = 2.4

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = float(input("Введите шаг"))                                            # Вводим значения 
x = x1

while x <= xn: # Пока х меньше или равен xn
  
  y = (math.log(a*x + 5))/(math.sqrt(a*x+2) + math.exp(x)) 
  print("при х = ", x, " y = ", y) # Печатаем формулу
  x=x+dx # и увеличиваем икс


#task 2

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = int(input("Введите шаг")) # Вводим значения 

for i in range(x1, xn, dx):  # цикл от начала до конца с шагом дельта икс 
  y = (math.log(a*x + 5))/(math.sqrt(a*x+2) + math.exp(x)) 
  print("при х = ", i, " y = ", y) # Выводим значение выражения


#task 3

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) # Вводим значения 

while (math.sin((n+1)*x))/(2*n+1) > e: # Пока значение больше эпсилон  
  f += (math.sin((n+1)*x))/(2*n+1) # Увеличиваем значение f
  n+=1 # Увеличиваем n
print('S = ', (f)) 

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) 

while n*(x)**(n-1) > e: # проверяем условие на эпсилон 
  f += ((-1)**(n-1))*n*(x)**(n-1) # увеличиваем ряд на конкретное значение на данном этапе 
  n+=1 # сдвигаем n по циклу дальше
print('S = ', (f)) # выводим итоговое значение 

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e")) 

while n*(x)**(n-1) > e: 
  f += ((-1)**(n-1))*n*(x)**(n-1) 
  n+=1 
print('S = ', (f))
