import math
a=1.93
b=3.48
c=0.2
x=float(input("введите х ")) # Вводим число 
y=(a* math.cos(x) +b*math.exp(math.sin(x)))/(math.log(x)+c*x**4) # формула из варианта  
print("y=",y) # выводим значение 
