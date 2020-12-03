import math

a=2.44
b=1.39
c=6.21
x=float(input("введите х "))

y = math.sqrt(x + math.exp(a*x)) * math.log((b*x**2 - 1)/(c*x**2 + 3))

print("y=",y)

