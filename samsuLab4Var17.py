import math

# task 1
a=1.57
b=2.38

x=float(input("введите х "))

if x<= -1:
  
  y = math.sqrt(abs(math.sin(a*x)))
  print ("y= ", y)
  
else:

  y=math.log(1 + (b*x)**2)
  print ("y= ", y)

# task 2

import math

a=2.7
b=1.5

x=float(input("введите х "))

if x <= -1:

  y = 1/(1+x)**2
  print ("y= ", y)

elif x > 1:

  y = x**2 + math.cos(a)
  print ("y= ", y)

else:
  y = math.sin(a*x + b)
  print ("y= ", y)
  
