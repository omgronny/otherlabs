import math


#task 1

a = 1.83
b = 2.27
x=float(input("введите х "))          # Вводим значение 

if x < -1:                            # Если  х меньше -1
  y = a + b*math.exp(x)               # Формула 
  print ("y = ", y)                   # Выводим значение 
else:
  y = math.cos((a*x)**2)**3           # Иначе другая формула 
  print ("y = ", y)                  


#task 2
a = 2.7
b = 2.4

x=float(input("введите х "))          # Вводим значение 
if x <= 3:                            # Если  х максимум 3
  y = math.sqrt(a*x**2 + 1)           # Формула
  print ("y = ", y)                   
elif x < 6 :                          # Иначе если х меньше 6
  y = math.log(b*x)                   # Формула
  print ("y = ", y)                   
else:
  y = math.cos((3*x**2)/(1+a*x))      # в остальных случаях третья формула      
  print ("y = ", y)                    

