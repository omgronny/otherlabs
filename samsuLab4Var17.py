import math

# task 1
a=1.57
b=2.38

x=float(input("введите х ")) # Вводим значение 

if x<= -1: # Если  х меньше -1
  
  y = math.sqrt(abs(math.sin(a*x))) # Формула
  print ("y= ", y) # Выводим значение 
  
else:

  y=math.log(1 + (b*x)**2) # Иначе другая формула 
  print ("y= ", y)

# task 2

import math

a=2.7
b=1.5

x=float(input("введите х ")) # Вводим значение 

if x <= -1: # Если  х максимум 3

  y = 1/(1+x)**2  # Формула
  print ("y= ", y) 

elif x > 1: # Иначе если х больше 1

  y = x**2 + math.cos(a) # Формула
  print ("y= ", y)

else:
  y = math.sin(a*x + b) # в остальных случаях третья формула  
  print ("y= ", y)
  
