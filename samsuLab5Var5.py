import math

#task 1

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = float(input("Введите шаг"))
x = x1

while x <= xn:
  
  y = (9*math.cos(x)) / (1 + (0.57**2)*(math.sin(x))**3)
  print("при х = ", x, " y = ", y)
  x=x+dx


#task 2

x1 = int(input("Введите начальное значение"))
xn = int(input("Введите конечное значение"))
dx = int(input("Введите шаг"))

for i in range(x1, xn, dx):
  y = (9*math.cos(i)) / (1 + (0.57**2)*(math.sin(i))**3)
  print("при х = ", i, " y = ", y)


#task 3

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e"))

while (x*math.sin(2*n-1))/(2*n-1) > e:
  f += (x*math.sin(2*n-1))/(2*n-1)
  n+=1
print('S = ', f*4*12/math.pi)

n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e"))

while (x*math.sin(2*n-1))/(2*n-1) > e:
  f += (x*math.sin(2*n-1))/(2*n-1)
  n+=1
print('S = ', f*4*17/math.pi)



n = 1
f = 0
x=float(input("Введите значение переменной х"))
e=float(input("Введите значение переменной e"))

while (x*math.sin(2*n-1))/(2*n-1) > e:
  f += (x*math.sin(2*n-1))/(2*n-1)
  n+=1
print('S = ', f*4*19/math.pi)
